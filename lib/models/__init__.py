# lib/models/__init__.py

import sqlite3
import os

# Database setup constants
DATABASE_FILE = "car_collection.db"
SQLITE_CONNECTION = sqlite3.connect(DATABASE_FILE)
CURSOR = SQLITE_CONNECTION.cursor()

def create_tables():
    """Create the necessary database tables if they don't exist"""
    
    # Cars table for storing car information
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            engine TEXT NOT NULL,
            horsepower INTEGER NOT NULL,
            price REAL NOT NULL,
            fuel_type TEXT DEFAULT 'Gasoline',
            date_added TEXT DEFAULT CURRENT_TIMESTAMP,
            is_custom BOOLEAN DEFAULT 0
        )
    ''')
    
    # Pre-populate with some sample cars if the table is empty
    CURSOR.execute('SELECT COUNT(*) FROM cars')
    if CURSOR.fetchone()[0] == 0:
        sample_cars = [
            ('Ferrari', '488 GTB', 2022, '3.9L Twin-Turbo V8', 661, 262000, 'Gasoline', '2024-01-01', 0),
            ('Lamborghini', 'Huracán', 2023, '5.2L V10', 630, 248295, 'Gasoline', '2024-01-01', 0),
            ('McLaren', '720S', 2022, '4.0L Twin-Turbo V8', 710, 299000, 'Gasoline', '2024-01-01', 0),
            ('Porsche', '911 Turbo S', 2023, '3.8L Twin-Turbo Flat-6', 640, 207000, 'Gasoline', '2024-01-01', 0),
            ('Bugatti', 'Chiron', 2023, '8.0L Quad-Turbo W16', 1479, 3300000, 'Gasoline', '2024-01-01', 0),
            ('Tesla', 'Model S Plaid', 2023, 'Electric Motors', 1020, 129990, 'Electric', '2024-01-01', 0),
            ('Aston Martin', 'DB11', 2022, '5.2L Twin-Turbo V12', 630, 205600, 'Gasoline', '2024-01-01', 0),
            ('Mercedes-AMG', 'GT 63 S', 2023, '4.0L Twin-Turbo V8', 630, 159500, 'Gasoline', '2024-01-01', 0),
            ('BMW', 'M8 Competition', 2023, '4.4L Twin-Turbo V8', 617, 146895, 'Gasoline', '2024-01-01', 0),
            ('Audi', 'R8 V10', 2022, '5.2L V10', 562, 148700, 'Gasoline', '2024-01-01', 0),
            ('Nissan', 'GT-R NISMO', 2023, '3.8L Twin-Turbo V6', 600, 215740, 'Gasoline', '2024-01-01', 0),
            ('Chevrolet', 'Corvette Z06', 2023, '5.5L V8', 670, 106395, 'Gasoline', '2024-01-01', 0),
            ('Ford', 'Mustang Shelby GT500', 2023, '5.2L Supercharged V8', 760, 80795, 'Gasoline', '2024-01-01', 0),
            ('Dodge', 'Challenger SRT Hellcat', 2023, '6.2L Supercharged V8', 717, 71490, 'Gasoline', '2024-01-01', 0),
            ('Acura', 'NSX Type S', 2022, 'Hybrid V6 + Electric Motors', 600, 169500, 'Hybrid', '2024-01-01', 0),
            ('Lexus', 'LC 500', 2023, '5.0L V8', 471, 97350, 'Gasoline', '2024-01-01', 0),
            ('Maserati', 'MC20', 2023, '3.0L Twin-Turbo V6', 621, 216995, 'Gasoline', '2024-01-01', 0),
            ('Koenigsegg', 'Regera', 2022, '5.0L Twin-Turbo V8 + Electric', 1500, 1900000, 'Hybrid', '2024-01-01', 0),
            ('Rimac', 'Nevera', 2023, 'Four Electric Motors', 1914, 2400000, 'Electric', '2024-01-01', 0)
        ]
        
        CURSOR.executemany('''
            INSERT INTO cars (make, model, year, engine, horsepower, price, fuel_type, date_added, is_custom)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', sample_cars)
    
    SQLITE_CONNECTION.commit()

# Initialize the database when the module is imported
create_tables()

def get_connection():
    """Get the database connection"""
    return SQLITE_CONNECTION

def get_cursor():
    """Get the database cursor"""
    return CURSOR