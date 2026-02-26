#!/usr/bin/env python3
"""
MySQL Query Script using Python
Usage: python3 query.py "SQL_QUERY" HOST PORT DATABASE USERNAME PASSWORD
"""

import sys
import re

def validate_query(query):
    """Validate that query is read-only"""
    query_upper = query.strip().upper()
    allowed_patterns = ['^SELECT', '^DESCRIBE', '^DESC', '^SHOW', '^EXPLAIN']
    
    for pattern in allowed_patterns:
        if re.match(pattern, query_upper):
            return True
    
    return False

def ensure_limit(query, default_limit=10):
    """Auto-append LIMIT if SELECT query has no LIMIT clause"""
    query_stripped = query.strip().rstrip(';')
    query_upper = query_stripped.upper()
    if query_upper.startswith('SELECT') and 'LIMIT' not in query_upper:
        query_stripped += f" LIMIT {default_limit}"
        print(f"[auto] 未指定 LIMIT，默认追加 LIMIT {default_limit}", file=sys.stderr)
    return query_stripped

def main():
    if len(sys.argv) < 6:
        print("Error: Missing required parameters")
        print("Usage: python3 query.py \"SQL_QUERY\" HOST PORT DATABASE USERNAME [PASSWORD]")
        sys.exit(1)
    
    query = sys.argv[1]
    host = sys.argv[2]
    port = int(sys.argv[3])
    database = sys.argv[4]
    username = sys.argv[5]
    password = sys.argv[6] if len(sys.argv) > 6 else ""
    
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
