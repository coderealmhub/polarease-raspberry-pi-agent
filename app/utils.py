import psutil

def get_info_raspbarrypi():
    cpu_info = psutil.cpu_percent(interval=1)
    cpu_temp = psutil.sensors_temperatures().get("cpu_thermal", None)

    # Verificar se cpu_temp é None antes de acessá-lo
    if cpu_temp is not None:
        cpu_temp_value = f"{cpu_temp[0].current}°C"
    else:
        cpu_temp_value = "N/A"

    ram_info = psutil.virtual_memory()
    ram_total = ram_info.total
    ram_used = ram_info.used
    ram_free = ram_info.available

    swap_info = psutil.swap_memory()
    swap_total = swap_info.total
    swap_used = swap_info.used
    swap_free = swap_info.free

    disk_info = psutil.disk_usage("/")
    disk_total = disk_info.total
    disk_used = disk_info.used
    disk_free = disk_info.free

    info = {
        "cpu_info": f"{cpu_info}%",
        "cpu_temp": cpu_temp_value,
        "ram_total": f"{ram_total} bytes",
        "ram_used": f"{ram_used} bytes",
        "ram_free": f"{ram_free} bytes",
        "swap_total": f"{swap_total} bytes",
        "swap_used": f"{swap_used} bytes",
        "swap_free": f"{swap_free} bytes",
        "disk_total": f"{disk_total} bytes",
        "disk_used": f"{disk_used} bytes",
        "disk_free": f"{disk_free} bytes",
    }

    return info