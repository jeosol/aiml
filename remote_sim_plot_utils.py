import matplotlib.pyplot as plt

def plot_field_results(field_results):
    """Make a sample plot of the oil production rate vs. time (in days)"""
    unit_system = field_results['unit-system']
    field_oil_rates = field_results["oil-prod-rates"]
    if unit_system.lower() == "field" :
        oil_unit = "(STB/D)"
    else:
        oil_unit = "(M3/D)"
    time_in_days   = field_results['time-days']
    plt.plot(time_in_days, field_oil_rates)
    plt.grid(True)
    plt.xlabel('Time (days)')
    plt.ylabel('Field Oil Rate ' + oil_unit)
    plt.title('Field Oil Production Rate vs. Time (days).')
               
