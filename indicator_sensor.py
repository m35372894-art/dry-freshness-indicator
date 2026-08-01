"""
Bio-Based Freshness Indicator Simulation
-----------------------------------------
Models pH shifts driven by TVB-N (Total Volatile Basic Nitrogen) 
gaseous accumulation and computes the corresponding anthocyanin 
sticker color response.
"""

from typing import Dict, Tuple

class FreshnessIndicator:
    def __init__(self, food_type: str = "Fish"):
        self.food_type = food_type
        
    def calculate_ph(self, storage_days: float, temperature_c: float) -> float:
        """
        Simulates pH increase inside package due to TVB-N gas release.
        Temperature accelerates spoilage rate according to Arrhenius kinetics.
        """
        base_ph = 6.0  # Fresh baseline pH
        # Temp factor: exponential growth above recommended 4°C storage
        temp_multiplier = 1.0 + max(0, (temperature_c - 4.0) * 0.15)
        
        # Simulated volatile nitrogen buildup over time
        tvb_n_mg = (storage_days ** 1.8) * 1.5 * temp_multiplier
        
        # pH increases as basic volatile amines (ammonia, TMA) accumulate
        calculated_ph = base_ph + (tvb_n_mg / 20.0)
        return min(round(calculated_ph, 2), 10.0)

    def get_color_response(self, ph: float) -> Dict[str, str]:
        """
        Maps current package micro-environment pH to the red cabbage 
        anthocyanin pigment color scale.
        """
        if ph <= 5.5:
            return {"status": "FRESH", "hex": "#8A2BE2", "color_name": "Purple/Pink"}
        elif 5.5 < ph <= 7.0:
            return {"status": "FRESH", "hex": "#4169E1", "color_name": "Royal Blue"}
        elif 7.0 < ph <= 8.5:
            return {"status": "EARLY SPOILAGE", "hex": "#2E8B57", "color_name": "Sea Green"}
        else:
            return {"status": "SPOILED", "hex": "#9ACD32", "color_name": "Yellow-Green"}

    def evaluate_food(self, days: float, temp_c: float) -> Tuple[float, Dict[str, str]]:
        current_ph = self.calculate_ph(days, temp_c)
        status = self.get_color_response(current_ph)
        return current_ph, status
