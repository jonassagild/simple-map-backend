from fastapi import APIRouter
import xarray as xr

router = APIRouter()

dataset_filename: str = "waves_2019-01-01.nc"

dataset = xr.open_dataset(dataset_filename)

@router.get("/max_wave_height_at_point/")
async def location_info(lat: float, lng: float):
    # Assume some complex calculation here
    max_wave_height = calculate_wave_height(lat, lng)
    return {"maximum_wave_height": max_wave_height}

def calculate_wave_height(lat: float, lng: float):
    # Implement your calculation logic here
    result = lat + lng  # Simple placeholder logic
    return result