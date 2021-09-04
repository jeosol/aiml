import matplotlib.pyplot as plt

def plot_field_results(field_results):
    """Make a sample plot of the oil production rate vs. time (in days)"""
    plt.figure()
    unit_system = field_results['unit-system']
    field_oil_rates = field_results["oil-prod-rates"]
    field_water_prod_rates = field_results["water-prod-rates"]
    field_water_inje_rates = field_results["water-inje-rates"]
    columns = ['oil-prod-rates', 'water-prod-rates', 'water-inje-rates']
    legends = ['Oil Production Rate', 'Water Production Rate', 'Water Injection Rate']        
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
    plt.ylabel('Fluid Rates' + rate_unit)
    plt.title('Field Production and Injection Rates vs. Time')
               
def plot_producer_results(results):
    """Make plot of relevant production quantities for producer wells"""
    plt.figure()
    unit_system = results['field_results']['unit-system']
    well_results = results['well_results']
    producer_well_names = results['producer_well_names']
    if unit_system.lower() == "field" :
        rate_unit = "(STB/D)"        
    else:
        rate_unit = "(M3/D)"
    for well_name in producer_well_names:
        curr_well_results = well_results[well_name]
        plt.plot(curr_well_results['time-days'], curr_well_results['oil-prod-rates'])    
    plt.legend(producer_well_names)
    plt.grid(True)
    plt.xlabel('Time (days)')
    plt.ylabel('Oil Production Rate ' + rate_unit)
    plt.title ('Well Oil Production Rates vs. Time')
    plt.figure()
    for well_name in producer_well_names:
        curr_well_results = well_results[well_name]
        plt.plot(curr_well_results['time-days'], curr_well_results['water-prod-rates'])
    plt.legend(producer_well_names)
    plt.grid(True)
    plt.xlabel('Time (days)')
    plt.ylabel('Water Production Rate ' + rate_unit)
    plt.title ('Well Water Production Rates vs. Time')
                    
def plot_injector_results(results):
    """Make plot of relevant quantities for injection wells"""
    plt.figure()
    unit_system = results['field_results']['unit-system']
    well_results = results['well_results']
    injector_well_names = results['injector_well_names']
    if unit_system.lower() == "field" :
        rate_unit = "psi"        
    else:
        rate_unit = "barsa"
    for well_name in injector_well_names:
        curr_well_results = well_results[well_name]
        plt.plot(curr_well_results['time-days'], curr_well_results['water-inje-rates'])    
    plt.legend(injector_well_names)
    plt.grid(True)
    plt.xlabel('Time (days)')
    plt.ylabel('Water Injection Rate ' + rate_unit)
    plt.title ('Well Water Injection Rate vs. Time')
    plt.figure()
    for well_name in injector_well_names:
        curr_well_results = well_results[well_name]
        plt.plot(curr_well_results['time-days'], curr_well_results['pressures'])
    plt.legend(injector_well_names)
    plt.grid(True)
    plt.xlabel('Time (days)')
    plt.ylabel('Well BHP ' + rate_unit)
    plt.title ('Well BHP Pressures vs. Time')
    