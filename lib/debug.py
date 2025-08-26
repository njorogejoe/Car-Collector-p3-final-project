#!/usr/bin/env python3
# lib/debug.py

"""
Debug script for Virtual Car Collection Manager
Use this script to test individual functions and debug the application
"""

from models.car import Car
from models import get_connection, get_cursor
import helpers

def test_database_connection():
    """Test if database connection is working"""
    try:
        cursor = get_cursor()
        cursor.execute("SELECT COUNT(*) FROM cars")
        count = cursor.fetchone()[0]
        print(f"✅ Database connection successful. Found {count} cars in database.")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def test_car_model():
    """Test Car model functionality"""
    print("\n🧪 Testing Car Model...")
    
    # Test getting all cars
    cars = Car.get_all()
    print(f"Total cars in database: {len(cars)}")
    
    if cars:
        # Test displaying first car
        first_car = cars[0]
        print(f"\nFirst car: {first_car}")
        print(first_car.display_details())
        
        # Test search functionality
        search_results = Car.search("Ferrari")
        print(f"\nFerrari search results: {len(search_results)} cars found")
        
        # Test statistics
        stats = Car.get_collection_stats()
        print(f"\nCollection statistics:")
        print(f"- Total value: ${stats['total_value']:,.2f}")
        print(f"- Average price: ${stats['avg_price']:,.2f}")

def create_test_custom_car():
    """Create a test custom car for debugging"""
    print("\n🧪 Creating test custom car...")
    
    test_car = Car(
        make="Debug Motors",
        model="Test Car 3000",
        year=2024,
        engine="Debug Engine V8",
        horsepower=999,
        price=123456.78,
        fuel_type="Test Fuel",
        is_custom=True
    )
    
    car_id = test_car.save()
    print(f"✅ Test car created with ID: {car_id}")
    print(test_car.display_details())
    
    return test_car

def cleanup_test_cars():
    """Remove any test cars created during debugging"""
    print("\n🧹 Cleaning up test cars...")
    
    cursor = get_cursor()
    connection = get_connection()
    
    cursor.execute("SELECT id FROM cars WHERE make = 'Debug Motors' OR model LIKE '%Test%'")
    test_car_ids = cursor.fetchall()
    
    if test_car_ids:
        for (car_id,) in test_car_ids:
            cursor.execute("DELETE FROM cars WHERE id = ?", (car_id,))
        connection.commit()
        print(f"✅ Removed {len(test_car_ids)} test cars")
    else:
        print("No test cars found to clean up")

def test_helpers():
    """Test helper functions"""
    print("\n🧪 Testing helper functions...")
    
    # Test stats
    try:
        stats = Car.get_collection_stats()
        print("✅ Collection stats function working")
    except Exception as e:
        print(f"❌ Collection stats error: {e}")
    
    # Test search
    try:
        results = Car.search("Tesla")
        print(f"✅ Search function working - found {len(results)} Tesla cars")
    except Exception as e:
        print(f"❌ Search function error: {e}")

def display_all_tables():
    """Display all database tables and their contents (for debugging)"""
    print("\n📊 Database Contents:")
    print("=" * 50)
    
    cursor = get_cursor()
    
    # Get table info
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    
    for (table_name,) in tables:
        print(f"\n📋 Table: {table_name}")
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 5")
        rows = cursor.fetchall()
        
        if rows:
            # Get column names
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = [col[1] for col in cursor.fetchall()]
            print(f"Columns: {', '.join(columns)}")
            print("Sample data:")
            for row in rows:
                print(f"  {row}")
        else:
            print("  (empty)")

def main():
    """Main debug function"""
    print("🔧 Virtual Car Collection Manager - Debug Mode")
    print("=" * 60)
    
    while True:
        print("\n🔧 Debug Menu:")
        print("1. Test database connection")
        print("2. Test Car model")
        print("3. Create test custom car")
        print("4. Test helper functions")
        print("5. Display database contents")
        print("6. Cleanup test cars")
        print("7. Run all tests")
        print("0. Exit debug mode")
        
        choice = input("\nSelect debug option: ").strip()
        
        if choice == "0":
            print("Exiting debug mode...")
            break
        elif choice == "1":
            test_database_connection()
        elif choice == "2":
            test_car_model()
        elif choice == "3":
            create_test_custom_car()
        elif choice == "4":
            test_helpers()
        elif choice == "5":
            display_all_tables()
        elif choice == "6":
            cleanup_test_cars()
        elif choice == "7":
            print("🚀 Running all tests...")
            test_database_connection()
            test_car_model()
            test_helpers()
            print("✅ All tests completed!")
        else:
            print("❌ Invalid choice")
        
        if choice != "0":
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()