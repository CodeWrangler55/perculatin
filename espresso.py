import numpy as np

class EspressoPercolationOptimizer:
    def __init__(self, water_temp, pressure, coffee_dose, desired_yield, brew_ratio):
        self.water_temp = water_temp
        self.pressure = pressure
        self.coffee_dose = coffee_dose
        self.desired_yield = desired_yield
        self.brew_ratio = brew_ratio
        self.data = []

    def add_trial(self, grind_size, flow_rate, extraction_time, yield_ml, tds):
        trial = {
            'grind_size': grind_size,
            'flow_rate': flow_rate,
            'extraction_time': extraction_time,
            'yield_ml': yield_ml,
            'tds': tds
        }
        self.data.append(trial)

    def calculate_extraction_yield(self, trial):
        return trial['yield_ml'] * trial['tds']

    def percolation_model(self, grind_size):
        p_threshold = 0.592  # Example critical threshold for 2D percolation
        connectivity = np.exp(-((grind_size - 300) / 50)**2)  # Adjusted Gaussian model for espresso grind size
        return connectivity, connectivity > p_threshold

    def optimize_grind_size(self):
        best_grind_size = None
        best_extraction_yield = 0
        best_uniformity = False
        
        for trial in self.data:
            grind_size = trial['grind_size']
            extraction_yield = self.calculate_extraction_yield(trial)
            connectivity, is_uniform = self.percolation_model(grind_size)
            
            if is_uniform and extraction_yield > best_extraction_yield:
                best_extraction_yield = extraction_yield
                best_grind_size = grind_size
                best_uniformity = is_uniform
        
        return best_grind_size, best_uniformity

def main():
    optimizer = EspressoPercolationOptimizer(water_temp=93, pressure=9, coffee_dose=18, desired_yield=36, brew_ratio=1.2)
    
    trials = [
        {'grind_size': 200, 'flow_rate': 2, 'extraction_time': 25, 'yield_ml': 36, 'tds': 9},
        {'grind_size': 250, 'flow_rate': 2.2, 'extraction_time': 27, 'yield_ml': 35, 'tds': 10},
        {'grind_size': 300, 'flow_rate': 2.5, 'extraction_time': 26, 'yield_ml': 36, 'tds': 11},
        {'grind_size': 350, 'flow_rate': 2.8, 'extraction_time': 28, 'yield_ml': 37, 'tds': 10},
        {'grind_size': 400, 'flow_rate': 3, 'extraction_time': 24, 'yield_ml': 34, 'tds': 9},
    ]

    for trial in trials:
        optimizer.add_trial(**trial)

    optimal_grind_size, is_optimal_uniform = optimizer.optimize_grind_size()
    
    print(f'Optimal grind size for espresso: {optimal_grind_size} microns')
    print(f'Is the optimal grind size achieving uniform percolation: {"Yes" if is_optimal_uniform else "No"}')

if __name__ == "__main__":
    main()
