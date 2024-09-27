def daily_anom(daily_var,clim=False):
    #daily climatology 
    var_clim = daily_var.groupby('time.dayofyear').mean('time').load()
    #daymean anomalies
    var_anom = daily_var.groupby('time.dayofyear') - var_clim
    if(clim==True):
        return var_anom, var_clim
    else:
        return var_anom
    
def monthly_anom(mon_var,clim=False):
    #monthly climatology 
    var_clim = mon_var.groupby('time.month').mean('time').load()
    #monthly anomalies
    var_anom = mon_var.groupby('time.month') - var_clim
    if(clim==True):
        return var_anom, var_clim
    else:
        return var_anom
