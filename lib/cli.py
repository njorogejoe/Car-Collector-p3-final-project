#!/usr/bin/env python3
# lib/cli.py

from helpers import (
    exit_program,
    browse_available_cars,
    add_existing_car,
    create_custom_car,
    view_my_collection,
    search_cars,
    compare_cars,
    view_collection_stats,
    export_collection,
    remove_from_collection,
    display_car_details
)

def main():
    """Main application loop"""
    print("🚗 Welcome to Virtual Car Collection Manager! 🏁")
    print("Build and manage your dream car collection!")
    
    while True:
        menu()
        choice = input("> ").strip()
        
        if choice == "0":
            exit_program()
        elif choice == "1":
            browse_available_cars()
        elif choice == "2":
            add_existing_car()
        elif choice == "3":
            create_custom_car()
        elif choice == "4":
            view_my_collection()
        elif choice == "5":
            search_cars()
        elif choice == "6":
            compare_cars()
        elif choice == "7":
            view_collection_stats()
        elif choice == "8":
            display_car_details()
        elif choice == "9":
            remove_from_collection()
        elif choice == "10":
            export_collection()
        else:
            print("❌ Invalid choice. Please select a valid option (0-10).")
        
        if choice != "0":
            input("\nPress Enter to continue...")

def menu():
    """Display the main menu options"""
    print("\n" + "=" * 60)
    print("🚗 VIRTUAL CAR COLLECTION MANAGER 🚗")
    print("=" * 60)
    print("📋 What would you like to do?")
    print()
    print("🔍 BROWSE & SEARCH:")
    print("   1. Browse all available cars")
    print("   2. Add existing car to my collection")
    print("   5. Search cars")
    print("   8. View detailed car information")
    print()
    print("🏠 MY COLLECTION:")
    print("   3. Create custom car")
    print("   4. View my collection")
    print("   9. Remove car from collection")
    print()
    print("📊 ANALYSIS & TOOLS:")
    print("   6. Compare two cars")
    print("   7. View collection statistics")
    print("   10. Export my collection")
    print()
    print("   0. Exit program")
    print("=" * 60)

if __name__ == "__main__":
    main()
