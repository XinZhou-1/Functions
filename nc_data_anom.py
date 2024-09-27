def daily_anom(daily_var,ystr,yend,clim=False):
    #daily climatology, from ystr to yend  
    var_clim = daily_var.sel(time = slice(f'{ystr}-01-01',f'{yend}-12-31')).groupby('time.dayofyear').mean('time').load()
    #daymean anomalies, relative to the climatology ystr-yend
    var_anom = daily_var.groupby('time.dayofyear') - var_clim
    if(clim==True):
        return var_anom, var_clim
    else:
        return var_anom
    
def monthly_anom(mon_var,ystr,yend,clim=False):
    #monthly climatology, from ystr to yend
    var_clim = mon_var.sel(time = slice(f'{ystr}-01-01',f'{yend}-12-31')).groupby('time.month').mean('time').load()
    #monthly anomalies, relative to the climatology ystr-yend
    var_anom = mon_var.groupby('time.month') - var_clim
    if(clim==True):
        return var_anom, var_clim
    else:
        return var_anom
