"""
    File : main.py
    Author : Stian Broen
    Date : 13.04.2022
    Description :

Entry-point and event-loop for the matching algorithm

"""

# from matching_library
import datetime

from libs.matchlib.prepare import organize_reserved_sales , organize_ordinary_sales , organize_routes , \
    organize_drivers
from libs.matchlib.actions import handle_failed_reservations, handle_failed_sales, handle_routes, handle_drives
from libs.commonlib.debug_sim_fullGraph import simulate_horten_fullGraph , delete_simulation

"""
    Function : create_simulation

    Description :


"""
def create_simulation() :
    delete_simulation()
    simulate_horten_fullGraph()
    print('SIMULATION (RE-) CREATED')

"""
    Function : iteration_fullGraph

    Description :


"""
def iteration_fullGraph(calc_time : datetime.datetime = datetime.datetime.utcnow()) :

    ok_reservations , failed_reservations = organize_reserved_sales(calc_time)
    handle_failed_reservations(
        ok_reservations     = ok_reservations     ,
        failed_reservations = failed_reservations ,
        calc_time           = calc_time
    )

    ok_sales , failed_sales = organize_ordinary_sales(calc_time)
    handle_failed_sales(
        ok_sales     = ok_sales     ,
        failed_sales = failed_sales ,
        calc_time    = calc_time
    )

    ok_drives , failed_drives = organize_drivers(calc_time)
    handle_drives(
        ok_drives     = ok_drives     ,
        failed_drives = failed_drives ,
        calc_time     = calc_time
    )

    routes = organize_routes(calc_time)
    handle_routes(
        routes    = routes    ,
        calc_time = calc_time ,
        is_fake   = True
    )

    print('ITERATION COMPLETED')

"""

    __main__

    Description :


"""
if __name__ == '__main__':

    #create_simulation()

    # All buyers get to buy :
    #calc_time = datetime.datetime.utcnow()
    #iteration_fullGraph(calc_time)

    # No buyer get to buy, its too soon
    #FOUR_DAYS_AHEAD = datetime.datetime.utcnow() + datetime.timedelta(days=4)
    #iteration_fullGraph(FOUR_DAYS_AHEAD)

    # All buyers can buy again, enough time has passed
    #SIX_DAYS_AHEAD = datetime.datetime.utcnow() + datetime.timedelta(days=6)
    #iteration_fullGraph(SIX_DAYS_AHEAD)

    # No buyer get to buy, its too soon
    #SEVEN_DAYS_AHEAD = datetime.datetime.utcnow() + datetime.timedelta(days=7)
    #iteration_fullGraph(SEVEN_DAYS_AHEAD)

    # Enough time has passed, but there is just enough bags for the reserving client (also reserved for next week)
    #FOURTEEN_DAYS_AHEAD = datetime.datetime.utcnow() + datetime.timedelta(days=14)
    #iteration_fullGraph(FOURTEEN_DAYS_AHEAD)

    #print('____')
    
    """
    Create a function "main_loop" which loops forever and calls on the iteration_fullGraph each iteration, including some time.sleep.
    Then call that function below :
    """
    #main_loop()



