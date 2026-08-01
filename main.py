from indicator_sensor import FreshnessIndicator

def run_simulation():
    sensor = FreshnessIndicator(food_type="Fish/Poultry")
    
    print("--- DIY Bio-Indicator Simulation Run ---")
    print("Testing food item stored at 4°C across 7 days:\n")
    
    for day in range(1, 8):
        ph, color_data = sensor.evaluate_food(days=day, temp_c=4.0)
        
        print(f"Day {day}:")
        print(f"  ├─ Estimated pH: {ph}")
        print(f"  ├─ Sticker Color: {color_data['color_name']} ({color_data['hex']})")
        print(f"  └─ Status: {color_data['status']}")
        print("-" * 40)

if __name__ == "__main__":
    run_simulation()
