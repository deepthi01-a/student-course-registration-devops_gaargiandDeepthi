#!/bin/sh
echo "⏳ Waiting for PostgreSQL to be ready..."
until pg_isready -h postgres -p 5432 -U postgres; do
sleep 2
done

echo "✅ PostgreSQL is ready, starting backend"
exec python run.py