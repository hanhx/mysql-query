#!/usr/bin/env python3
"""
MySQL Query Script with Config Support
Usage: 
  python3 query_with_config.py --config test "SQL_QUERY"
  python3 query_with_config.py --host HOST --port PORT --database DB --user USER --password PASS "SQL_QUERY"
"""

import sys
import json
import os
import argparse
from pathlib import Path

# Import the main query function
sys.path.insert(0, os.path.dirname(__file__))
from query import validate_query, ensure_limit

def load_config(config_name):
    """Load database connection from config file"""
    config_file = Path(__file__).parent.parent / "config.json"
    
    if not config_file.exists():
        print(f"Error: Config file not found: {config_file}")
        print("Please create config.json based on config.example.json")
        sys.exit(1)
    
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
        
        if config_name not in config.get('connections', {}):
            print(f"Error: Connection '{config_name}' not found in config")
            print(f"Available connections: {', '.join(config['connections'].keys())}")
            sys.exit(1)
        
        return config['connections'][config_name]
    except Exception as e:
        print(f"Error loading config: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='MySQL Query Tool with Config Support')
    parser.add_argument('query', help='SQL query to execute')
    parser.add_argument('--config', '-c', help='Config name from config.json')
    parser.add_argument('--host', help='MySQL host')
    parser.add_argument('--port', type=int, default=3306, help='MySQL port')
    parser.add_argument('--database', '-d', help='Database name')
    parser.add_argument('--user', '-u', help='MySQL username')
    parser.add_argument('--password', '-p', default='', help='MySQL password')
    
    args = parser.parse_args()
    
    # Get connection info from config or arguments
    if args.config:
        conn = load_config(args.config)
        host = conn['host']
        port = conn['port']
        database = conn['database']
        username = conn['username']
        password = conn.get('password', '')
        print(f"Using config: {args.config} - {conn.get('description', '')}")
    else:
        if not all([args.host, args.database, args.user]):
            print("Error: --host, --database, and --user are required when not using --config")
            sys.exit(1)
        host = args.host
        port = args.port
        database = args.database
        username = args.user
        password = args.password
    
    query = args.query
    
    # Validate query is read-only
    if not validate_query(query):
        print("Error: Only SELECT, DESCRIBE, SHOW, and EXPLAIN queries are allowed")
        sys.exit(1)
    
    query = ensure_limit(query)
    
    try:
        import pymysql
    except ImportError:
        print("Error: pymysql is not installed")
        print("Please install it: pip3 install pymysql")
        sys.exit(1)
    
    try:
        # Connect to database
        connection = pymysql.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            database=database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                results = cursor.fetchall()
                
                if not results:
                    print("No results found")
                    return
                
                # Print results in a formatted way
                if isinstance(results[0], dict):
                    # Print header
                    headers = list(results[0].keys())
                    print(" | ".join(headers))
                    print("-" * (sum(len(h) for h in headers) + len(headers) * 3))
                    
                    # Print rows
                    for row in results:
                        print(" | ".join(str(row.get(h, '')) for h in headers))
                else:
                    for row in results:
                        print(row)
    
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
