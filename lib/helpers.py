# lib/helpers.py

import json
import os
from datetime import datetime
from models.car import Car

def exit_program():
    """Exit the program with a goodbye message"""
    print("\n🚗 Thanks for using Virtual Car Collection Manager!")
    print("Your garage is always waiting for you. Goodbye! 🏁")
    exit()

def browse_available_cars():
    """Display all available cars in the database"""
    print("\n🚗 Available Cars in Database:")
    print("=" * 90)
    
    cars = Car.get_all()
    
    if not cars:
        print("No cars found in the database.")
        return
    
    # Group cars by make for better organization
    cars_by_make = {}
    for car in cars:
        if car.make not in cars_by_make:
            cars_by_make[car.make] = []
        cars_by_make[car.make].append(car)
    
    for make in sorted(cars_by_make.keys()):
        print(f"\n📍 {make}:")
        for car in sorted(cars_by_make[make], key=lambda x: x.model):
            custom_tag = " (Custom)" if car.is_custom else ""
            print(f"   ID: {car.id:2d} | {car.year} {car.model}{custom_tag} | {car.horsepower:,} HP | ${car.price:,.2f}")

def add_existing_car():
    """Add an existing car from the database to collection"""
    browse_available_cars()
    
    try:
        car_id = int(input("\nEnter the ID of the car you want to add to your collection: "))
        car = Car.get_by_id(car_id)
        
        if car:
            if car.is_custom:
                print(f"\n✅ This custom car is already in your collection!")
            else:
                # Create a copy in the user's collection
                new_car = Car(
                    make=car.make,
                    model=car.model,
                    year=car.year,
                    engine=car.engine,
                    horsepower=car.horsepower,
                    price=car.price,
                    fuel_type=car.fuel_type,
                    is_custom=True  # Mark as part of user's collection
                )
                new_car.save()
                print(f"\n✅ Successfully added {car} to your collection!")
                print(car.display_details())
        else:
            print(f"❌ No car found with ID {car_id}")
            
    except ValueError:
        print("❌ Please enter a valid car ID number.")

def create_custom_car():
    """Create a new custom car and add it to the collection"""
    print("\n🔧 Create Your Custom Car")
    print("=" * 40)
    
    try:
        make = input("Enter car make (e.g., Ferrari, Tesla): ").strip()
        if not make:
            print("❌ Make is required.")
            return
            
        model = input("Enter car model (e.g., 488 GTB, Model S): ").strip()
        if not model:
            print("❌ Model is required.")
            return
        
        year = int(input("Enter year (e.g., 2023): "))
        if year < 1886 or year > 2030:  # First car was made in 1886
            print("❌ Please enter a reasonable year (1886-2030).")
            return
            
        engine = input("Enter engine specification (e.g., 3.9L Twin-Turbo V8): ").strip()
        if not engine:
            print("❌ Engine specification is required.")
            return
            
        horsepower = int(input("Enter horsepower (e.g., 661): "))
        if horsepower < 1 or horsepower > 5000:
            print("❌ Please enter a reasonable horsepower (1-5000).")
            return
            
        price = float(input("Enter price in USD (e.g., 262000): "))
        if price < 0:
            print("❌ Price cannot be negative.")
            return
        
        print("\nFuel type options: Gasoline, Electric, Hybrid, Diesel")
        fuel_type = input("Enter fuel type (default: Gasoline): ").strip() or "Gasoline"
        
        # Create and save the custom car
        custom_car = Car(
            make=make,
            model=model,
            year=year,
            engine=engine,
            horsepower=horsepower,
            price=price,
            fuel_type=fuel_type,
            is_custom=True
        )
        
        custom_car.save()
        print(f"\n✅ Successfully created your custom {custom_car}!")
        print(custom_car.display_details())
        
    except ValueError:
        print("❌ Please enter valid numeric values for year, horsepower, and price.")

def view_my_collection():
    """Display only cars in user's collection (custom cars)"""
    print("\n🏠 Your Personal Car Collection:")
    print("=" * 90)
    
    cars = [car for car in Car.get_all() if car.is_custom]
    
    if not cars:
        print("Your collection is empty. Add some cars to get started!")
        return
    
    for i, car in enumerate(cars, 1):
        print(f"\n{i}. {car}")
        print(f"   🔧 Engine: {car.engine}")
        print(f"   ⚡ Power: {car.horsepower:,} HP")
        print(f"   💰 Value: ${car.price:,.2f}")
        print(f"   ⛽ Fuel: {car.fuel_type}")
        print(f"   📅 Added: {car.date_added}")

def search_cars():
    """Search for cars by make, model, or fuel type"""
    query = input("\nEnter search term (make, model, or fuel type): ").strip()
    
    if not query:
        print("❌ Please enter a search term.")
        return
    
    cars = Car.search(query)
    
    if not cars:
        print(f"No cars found matching '{query}'")
        return
    
    print(f"\n🔍 Search Results for '{query}' ({len(cars)} found):")
    print("=" * 90)
    
    for car in cars:
        custom_tag = " (In Collection)" if car.is_custom else " (Available)"
        print(f"ID: {car.id:2d} | {car} | {car.horsepower:,} HP | ${car.price:,.2f}{custom_tag}")

def compare_cars():
    """Compare two cars side by side"""
    print("\n⚖️  Car Comparison Tool")
    print("=" * 40)
    
    try:
        car1_id = int(input("Enter first car ID: "))
        car2_id = int(input("Enter second car ID: "))
        
        car1 = Car.get_by_id(car1_id)
        car2 = Car.get_by_id(car2_id)
        
        if not car1:
            print(f"❌ No car found with ID {car1_id}")
            return
        if not car2:
            print(f"❌ No car found with ID {car2_id}")
            return
        
        print(f"\n⚖️  Comparing {car1} vs {car2}")
        print("=" * 100)
        
        # Comparison table
        print(f"{'Attribute':<15} | {'Car 1':<35} | {'Car 2':<35} | {'Winner':<10}")
        print("-" * 100)
        print(f"{'Make/Model':<15} | {f'{car1.make} {car1.model}':<35} | {f'{car2.make} {car2.model}':<35} | {'-':<10}")
        print(f"{'Year':<15} | {car1.year:<35} | {car2.year:<35} | {('Car 1' if car1.year > car2.year else 'Car 2' if car2.year > car1.year else 'Tie'):<10}")
        print(f"{'Horsepower':<15} | {f'{car1.horsepower:,} HP':<35} | {f'{car2.horsepower:,} HP':<35} | {('Car 1' if car1.horsepower > car2.horsepower else 'Car 2' if car2.horsepower > car1.horsepower else 'Tie'):<10}")
        print(f"{'Price':<15} | {f'${car1.price:,.2f}':<35} | {f'${car2.price:,.2f}':<35} | {('Car 2' if car1.price > car2.price else 'Car 1' if car2.price > car1.price else 'Tie'):<10}")
        print(f"{'Fuel Type':<15} | {car1.fuel_type:<35} | {car2.fuel_type:<35} | {'-':<10}")
        print(f"{'Engine':<15} | {car1.engine:<35} | {car2.engine:<35} | {'-':<10}")
        
        # Power-to-price ratio
        ppr1 = car1.horsepower / car1.price * 1000  # HP per $1000
        ppr2 = car2.horsepower / car2.price * 1000
        print(f"{'HP per $1000':<15} | {f'{ppr1:.2f}':<35} | {f'{ppr2:.2f}':<35} | {('Car 1' if ppr1 > ppr2 else 'Car 2' if ppr2 > ppr1 else 'Tie'):<10}")
        
    except ValueError:
        print("❌ Please enter valid car ID numbers.")

def view_collection_stats():
    """Display statistics about the car collection"""
    stats = Car.get_collection_stats()
    
    print("\n📊 Collection Statistics")
    print("=" * 50)
    print(f"Total Cars in Database: {stats['total_cars']}")
    print(f"Total Collection Value: ${stats['total_value']:,.2f}")
    print(f"Average Car Price: ${stats['avg_price']:,.2f}")
    
    if stats['most_expensive']:
        make, model, price = stats['most_expensive']
        print(f"Most Expensive Car: {make} {model} (${price:,.2f})")
    
    print("\n🔋 Fuel Type Breakdown:")
    for fuel_type, count in stats['fuel_breakdown'].items():
        percentage = (count / stats['total_cars']) * 100
        print(f"  {fuel_type}: {count} cars ({percentage:.1f}%)")
    
    print("\n🏭 Top 5 Manufacturers:")
    for make, count in stats['make_breakdown'].items():
        percentage = (count / stats['total_cars']) * 100
        print(f"  {make}: {count} cars ({percentage:.1f}%)")

def export_collection():
    """Export the user's collection to a text file"""
    my_cars = [car for car in Car.get_all() if car.is_custom]
    
    if not my_cars:
        print("❌ Your collection is empty. Add some cars first!")
        return
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"my_car_collection_{timestamp}.txt"
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write("🚗 MY VIRTUAL CAR COLLECTION 🚗\n")
            f.write("=" * 50 + "\n")
            f.write(f"Exported on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Cars: {len(my_cars)}\n")
            f.write(f"Total Value: ${sum(car.price for car in my_cars):,.2f}\n\n")
            
            for i, car in enumerate(my_cars, 1):
                f.write(f"{i}. {car.year} {car.make} {car.model}\n")
                f.write(f"   Engine: {car.engine}\n")
                f.write(f"   Power: {car.horsepower:,} HP\n")
                f.write(f"   Price: ${car.price:,.2f}\n")
                f.write(f"   Fuel Type: {car.fuel_type}\n")
                f.write(f"   Date Added: {car.date_added}\n\n")
            
            f.write("-" * 50 + "\n")
            f.write("Generated by Virtual Car Collection Manager\n")
        
        print(f"✅ Collection exported to: {filename}")
        print(f"📄 File contains {len(my_cars)} cars with complete details.")
        
    except Exception as e:
        print(f"❌ Error exporting collection: {e}")

def remove_from_collection():
    """Remove a car from the user's collection"""
    my_cars = [car for car in Car.get_all() if car.is_custom]
    
    if not my_cars:
        print("❌ Your collection is empty. Nothing to remove!")
        return
    
    print("\n🗑️  Your Cars:")
    for i, car in enumerate(my_cars, 1):
        print(f"{i}. ID: {car.id} | {car} | ${car.price:,.2f}")
    
    try:
        choice = int(input("\nEnter the number of the car to remove: "))
        if 1 <= choice <= len(my_cars):
            car_to_remove = my_cars[choice - 1]
            confirm = input(f"Are you sure you want to remove {car_to_remove} from your collection? (y/N): ").lower().strip()
            
            if confirm == 'y':
                car_to_remove.delete()
                print(f"✅ Removed {car_to_remove} from your collection.")
            else:
                print("❌ Removal cancelled.")
        else:
            print("❌ Invalid choice. Please enter a valid number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def display_car_details():
    """Display detailed information about a specific car"""
    try:
        car_id = int(input("\nEnter car ID to view details: "))
        car = Car.get_by_id(car_id)
        
        if car:
            print(car.display_details())
        else:
            print(f"❌ No car found with ID {car_id}")
            
    except ValueError:
        print("❌ Please enter a valid car ID number.")