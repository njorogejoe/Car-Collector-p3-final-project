# lib/models/car.py

from . import get_connection, get_cursor
from datetime import datetime

class Car:
    def __init__(self, make, model, year, engine, horsepower, price, fuel_type="Gasoline", car_id=None, date_added=None, is_custom=False):
        """
        Initialize a Car object.
        
        Args:
            make (str): Car manufacturer
            model (str): Car model name
            year (int): Year of manufacture
            engine (str): Engine specification
            horsepower (int): Engine horsepower
            price (float): Car price in USD
            fuel_type (str): Type of fuel (Gasoline, Electric, Hybrid)
            car_id (int): Database ID (for existing cars)
            date_added (str): Date when car was added to collection
            is_custom (bool): Whether this is a custom user-created car
        """
        self.id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine
        self.horsepower = horsepower
        self.price = price
        self.fuel_type = fuel_type
        self.date_added = date_added or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.is_custom = is_custom
    
    def save(self):
        """Save the car to the database"""
        cursor = get_cursor()
        connection = get_connection()
        
        if self.id is None:
            # Insert new car
            cursor.execute('''
                INSERT INTO cars (make, model, year, engine, horsepower, price, fuel_type, date_added, is_custom)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (self.make, self.model, self.year, self.engine, self.horsepower, 
                  self.price, self.fuel_type, self.date_added, self.is_custom))
            self.id = cursor.lastrowid
        else:
            # Update existing car
            cursor.execute('''
                UPDATE cars SET make=?, model=?, year=?, engine=?, horsepower=?, 
                               price=?, fuel_type=?, is_custom=?
                WHERE id=?
            ''', (self.make, self.model, self.year, self.engine, self.horsepower,
                  self.price, self.fuel_type, self.is_custom, self.id))
        
        connection.commit()
        return self.id
    
    def delete(self):
        """Delete the car from the database"""
        if self.id is not None:
            cursor = get_cursor()
            connection = get_connection()
            cursor.execute('DELETE FROM cars WHERE id=?', (self.id,))
            connection.commit()
            return True
        return False
    
    @classmethod
    def get_all(cls):
        """Get all cars from the database"""
        cursor = get_cursor()
        cursor.execute('''
            SELECT id, make, model, year, engine, horsepower, price, fuel_type, date_added, is_custom
            FROM cars ORDER BY make, model
        ''')
        
        cars = []
        for row in cursor.fetchall():
            car = cls(
                make=row[1], model=row[2], year=row[3], engine=row[4],
                horsepower=row[5], price=row[6], fuel_type=row[7],
                car_id=row[0], date_added=row[8], is_custom=bool(row[9])
            )
            cars.append(car)
        return cars
    
    @classmethod
    def get_by_id(cls, car_id):
        """Get a specific car by ID"""
        cursor = get_cursor()
        cursor.execute('''
            SELECT id, make, model, year, engine, horsepower, price, fuel_type, date_added, is_custom
            FROM cars WHERE id=?
        ''', (car_id,))
        
        row = cursor.fetchone()
        if row:
            return cls(
                make=row[1], model=row[2], year=row[3], engine=row[4],
                horsepower=row[5], price=row[6], fuel_type=row[7],
                car_id=row[0], date_added=row[8], is_custom=bool(row[9])
            )
        return None
    
    @classmethod
    def search(cls, query):
        """Search cars by make, model, or fuel type"""
        cursor = get_cursor()
        search_term = f"%{query}%"
        cursor.execute('''
            SELECT id, make, model, year, engine, horsepower, price, fuel_type, date_added, is_custom
            FROM cars 
            WHERE LOWER(make) LIKE LOWER(?) OR LOWER(model) LIKE LOWER(?) OR LOWER(fuel_type) LIKE LOWER(?)
            ORDER BY make, model
        ''', (search_term, search_term, search_term))
        
        cars = []
        for row in cursor.fetchall():
            car = cls(
                make=row[1], model=row[2], year=row[3], engine=row[4],
                horsepower=row[5], price=row[6], fuel_type=row[7],
                car_id=row[0], date_added=row[8], is_custom=bool(row[9])
            )
            cars.append(car)
        return cars
    
    @classmethod
    def get_collection_stats(cls):
        """Get statistics about the car collection"""
        cursor = get_cursor()
        
        # Total cars
        cursor.execute('SELECT COUNT(*) FROM cars')
        total_cars = cursor.fetchone()[0]
        
        # Total value
        cursor.execute('SELECT SUM(price) FROM cars')
        total_value = cursor.fetchone()[0] or 0
        
        # Average price
        cursor.execute('SELECT AVG(price) FROM cars')
        avg_price = cursor.fetchone()[0] or 0
        
        # Most expensive car
        cursor.execute('SELECT make, model, price FROM cars ORDER BY price DESC LIMIT 1')
        most_expensive = cursor.fetchone()
        
        # Fuel type breakdown
        cursor.execute('SELECT fuel_type, COUNT(*) FROM cars GROUP BY fuel_type')
        fuel_breakdown = dict(cursor.fetchall())
        
        # Make breakdown
        cursor.execute('SELECT make, COUNT(*) FROM cars GROUP BY make ORDER BY COUNT(*) DESC LIMIT 5')
        make_breakdown = dict(cursor.fetchall())
        
        return {
            'total_cars': total_cars,
            'total_value': total_value,
            'avg_price': avg_price,
            'most_expensive': most_expensive,
            'fuel_breakdown': fuel_breakdown,
            'make_breakdown': make_breakdown
        }
    
    def __str__(self):
        """String representation of the car"""
        return f"{self.year} {self.make} {self.model}"
    
    def __repr__(self):
        """Detailed representation of the car"""
        return f"Car(id={self.id}, make='{self.make}', model='{self.model}', year={self.year})"
    
    def display_details(self):
        """Return a formatted string with all car details"""
        custom_indicator = " (Custom)" if self.is_custom else ""
        return f"""
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║ {self.year} {self.make} {self.model}{custom_indicator:<20} ID: {self.id or 'N/A':<10} ║
╠══════════════════════════════════════════════════════════════════════════════════════════╣
║ Engine:      {self.engine:<70} ║
║ Power:       {self.horsepower:,} HP{'':<63} ║
║ Price:       ${self.price:,.2f}{'':<62} ║
║ Fuel Type:   {self.fuel_type:<70} ║
║ Added:       {self.date_added:<70} ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝
        """.strip()
    
    def to_dict(self):
        """Convert car to dictionary for export"""
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'engine': self.engine,
            'horsepower': self.horsepower,
            'price': self.price,
            'fuel_type': self.fuel_type,
            'date_added': self.date_added,
            'is_custom': self.is_custom
        }