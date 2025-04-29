import asyncpg
import asyncio

DATABASE_URL = "postgresql://dae22:1998@localhost/mydatabase"

async def create_table():
    conn = await asyncpg.connect(DATABASE_URL)
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    await conn.close()

asyncio.run(create_table())