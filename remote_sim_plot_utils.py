import matplotlib.pyplot as plt

def plot_field_results(field_results):
    """Make a sample plot of the oil production rate vs. time (in days)"""
    unit_system = field_results['unit-system']
    field_oil_rates = field_results["oil-prod-rates"]
    field_water_prod_rates = field_results["water-prod-rates"]
    field_water_inje_rates = field_results["water-inje-rates"]
    columns = ['oil-prod-rates', 'water-prod-rates', 'water-inje-rates']
    legends = ['Oil Prod. Rates', 'Water Prod. Rates', 'Water Inje. Rates']        
    if unit_system.lower() == "field" :
        rate_unit = "(STB/D)"        
    else:
        rate_unit = "(M3/D)"
        
    time_in_days   = field_results['time-days']
    #plt.plot(time_in_days, field_oil_rates)
    for column in columns:
        plt.plot(time_in_days, field_results[column])
        
    #plt.plot(time_in_days, field_oil_rates, time_in_days, field_water_prod_rates, )
    plt.legend(legends)
    plt.grid(True)
    plt.xlabel('Time (days)')
    plt.ylabel('Oil, Water Prod. Rates' + rate_unit)
    plt.title('Field Production and Injection Rates vs. Time')
               
