#!/bin/bash

# MySQL Query Script
# Usage: bash query.sh "SQL_QUERY" HOST PORT DATABASE USERNAME PASSWORD

QUERY="$1"
HOST="${2:-localhost}"
PORT="${3:-3306}"
DATABASE="$4"
USERNAME="$5"
PASSWORD="$6"

# Validate required parameters
if [ -z "$QUERY" ] || [ -z "$DATABASE" ] || [ -z "$USERNAME" ]; then
    echo "Error: Missing required parameters"
    echo "Usage: bash query.sh \"SQL_QUERY\" HOST PORT DATABASE USERNAME PASSWORD"
    exit 1
fi

# Security check: only allow read-only queries
QUERY_UPPER=$(echo "$QUERY" | tr '[:lower:]' '[:upper:]')
if [[ ! "$QUERY_UPPER" =~ ^(SELECT|DESCRIBE|DESC|SHOW|EXPLAIN) ]]; then
    echo "Error: Only SELECT, DESCRIBE, SHOW, and EXPLAIN queries are allowed"
    exit 1
fi

# Check if mysql client is installed
if ! command -v mysql &> /dev/null; then
    echo "Error: mysql client is not installed"
    echo "Please install MySQL client:"
    echo "  macOS: brew install mysql-client"
    echo "  Ubuntu/Debian: sudo apt-get install mysql-client"
    exit 1
fi

# Execute query
if [ -z "$PASSWORD" ]; then
    mysql -h "$HOST" -P "$PORT" -u "$USERNAME" "$DATABASE" -e "$QUERY"
else
    mysql -h "$HOST" -P "$PORT" -u "$USERNAME" -p"$PASSWORD" "$DATABASE" -e "$QUERY"
fi

exit $?
