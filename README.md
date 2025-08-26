# Virtual Car Collection Manager 🚗

A Python CLI application that lets car enthusiasts build and manage their dream car collection virtually. Browse supercars, add them to your garage, create custom vehicles, and analyze your collection with detailed statistics.

## Features ✨

- **Browse Car Database**: Explore 19 pre-loaded supercars and sports cars with realistic specifications
- **Personal Collection**: Build your own virtual garage by adding cars from the database
- **Custom Cars**: Create your own dream cars with custom specifications
- **Advanced Search**: Find cars by make, model, or fuel type
- **Car Comparison**: Compare any two cars side-by-side with detailed metrics
- **Collection Analytics**: View statistics including total value, fuel type breakdown, and manufacturer distribution
- **Export Functionality**: Export your collection to a text file for sharing or backup
- **Database Persistence**: All data is saved using SQLite database

## Installation & Setup 🛠️

1. **Clone or download** this repository
2. **Navigate** to the project directory
3. **Install dependencies**:
   ```bash
   pipenv install
   pipenv shell
   ```
4. **Run the application**:
   ```bash
   python lib/cli.py
   ```

## Project Structure 📁

```
car-collection-manager/
├── Pipfile                 # Python dependencies
├── README.md              # This file
└── lib/
    ├── cli.py            # Main CLI interface
    ├── helpers.py        # Helper functions for all features
    ├── debug.py          # Debug utilities and testing
    └── models/
        ├── __init__.py   # Database setup and configuration
        └── car.py        # Car model class with database methods
```

## File Descriptions 📄

### `lib/cli.py`
The main command-line interface that presents the user menu and handles user input. Contains the main program loop and menu system with 11 different options for managing your car collection.

### `lib/helpers.py`
Contains all the core functionality functions:
- `browse_available_cars()` - Display all cars in the database organized by manufacturer
- `add_existing_car()` - Add a car from the database to your personal collection
- `create_custom_car()` - Create a new car with custom specifications
- `view_my_collection()` - Display only cars in your personal collection
- `search_cars()` - Search functionality with partial matching
- `compare_cars()` - Side-by-side comparison tool with winner analysis
- `view_collection_stats()` - Statistical analysis of the entire database
- `export_collection()` - Export personal collection to timestamped text file
- `remove_from_collection()` - Remove cars from your personal collection
- `display_car_details()` - Show detailed information for any specific car

### `lib/models/car.py`
The Car class model that handles all database operations:
- **Car object creation** with comprehensive attributes (make, model, year, engine, horsepower, price, fuel type)
- **Database methods**: save(), delete(), get_all(), get_by_id(), search()
- **Statistical methods**: get_collection_stats() for analytics
- **Display methods**: Formatted output for car details and comparisons
- **Data export**: Dictionary conversion for file exports

### `lib/models/__init__.py`
Database initialization and configuration:
- **SQLite database setup** with automatic table creation
- **Pre-populated with 19 realistic supercars** including Ferrari 488 GTB, Lamborghini Huracán, McLaren 720S, Bugatti Chiron, Tesla Model S Plaid, and more
- **Connection management** utilities for database operations

### `lib/debug.py`
Development and debugging utilities:
- **Database connection testing** to ensure SQLite is working properly
- **Model testing functions** to verify Car class methods
- **Test data creation** for development purposes
- **Database content inspection** tools for troubleshooting
- **Cleanup utilities** to remove test data

## Car Database 🏎️

The application comes pre-loaded with 19 realistic supercars and sports cars:

**Electric/Hybrid Supercars:**
- Tesla Model S Plaid (1,020 HP) - $129,990
- Rimac Nevera (1,914 HP) - $2,400,000
- Acura NSX Type S (Hybrid, 600 HP) - $169,500
- Koenigsegg Regera (Hybrid, 1,500 HP) - $1,900,000

**European Supercars:**
- Bugatti Chiron (1,479 HP) - $3,300,000
- Ferrari 488 GTB (661 HP) - $262,000
- Lamborghini Huracán (630 HP) - $248,295
- McLaren 720S (710 HP) - $299,000
- Aston Martin DB11 (630 HP) - $205,600
- Maserati MC20 (621 HP) - $216,995

**German Performance Cars:**
- Porsche 911 Turbo S (640 HP) - $207,000
- Mercedes-AMG GT 63 S (630 HP) - $159,500
- BMW M8 Competition (617 HP) - $146,895
- Audi R8 V10 (562 HP) - $148,700

**American Muscle:**
- Chevrolet Corvette Z06 (670 HP) - $106,395
- Ford Mustang Shelby GT500 (760 HP) - $80,795
- Dodge Challenger SRT Hellcat (717 HP) - $71,490

**Japanese Performance:**
- Nissan GT-R NISMO (600 HP) - $215,740
- Lexus LC 500 (471 HP) - $97,350

## Usage Examples 💡

### Adding Cars to Your Collection
1. Choose option 1 to browse available cars
2. Note the ID of cars you want to add
3. Choose option 2 and enter the car ID
4. The car will be copied to your personal collection

### Creating Custom Cars
1. Choose option 3 for custom car creation
2. Enter specifications: make, model, year, engine, horsepower, price, fuel type
3. The car is automatically saved to your collection

### Comparing Cars
1. Choose option 6 for car comparison
2. Enter two car IDs (from any cars in the database)
3. View side-by-side comparison including power-to-price ratio and winners in each category

### Viewing Statistics
Option 7 provides comprehensive analytics:
- Total cars and collection value
- Average car price and most expensive vehicle
- Fuel type distribution (percentage breakdown)
- Top 5 manufacturers by car count

## Technical Details ⚙️

- **Language**: Python 3.8+
- **Database**: SQLite (no external database server required)
- **Dependencies**: None (uses only Python standard library)
- **Data Persistence**: All cars and collections are saved automatically
- **File Export**: Collections export to timestamped `.txt` files
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Development & Debugging 🔧

Use `python lib/debug.py` to access debugging utilities:
- Test database connections
- Verify all functions are working correctly
- Create test data for development
- Inspect database contents
- Clean up test data

## Future Enhancement Ideas 🚀

- **Car Maintenance Tracking**: Add service records and maintenance schedules
- **Racing Statistics**: Track virtual race performance and lap times
- **Car Trading System**: Allow users to trade cars with each other
- **Photo Integration**: Add car images and photo galleries
- **Advanced Filtering**: More complex search criteria and sorting options
- **Collection Goals**: Set and track collection milestones and achievements
- **Market Trends**: Track car value changes over time
- **Insurance Calculator**: Estimate insurance costs for different cars

## Contributing 🤝

Feel free to fork this project and submit pull requests with improvements. Some areas for contribution:
- Adding more car data to the database
- Implementing additional statistical analysis
- Creating new export formats (JSON, CSV)
- Adding data visualization features
- Improving the user interface design

## License 📜

This project is open source and available under standard educational use terms.

---

**Happy collecting! 🏁** Build your dream garage and explore the world of supercars virtually!