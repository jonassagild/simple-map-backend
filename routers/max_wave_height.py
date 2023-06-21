from fastapi import APIRouter
import xarray as xr
import math

router = APIRouter()

dataset_filename: str = "waves_2019-01-01.nc"

dataset: xr.Dataset = xr.open_dataset(dataset_filename)
hmax_data_array: xr.DataArray = dataset.hmax


@router.get("/max_wave_height_at_point/")
async def max_wave_height_at_point(lat: float, lng: float):
    """Max_wave_height_at_point handler."""
    params_valid = validate_request_params(lat, lng)
    if params_valid:
        calc_valid, max_wave_height = calculate_approx_max_wave_height(
            lat, lng)
    else:
        calc_valid = False
        max_wave_height = 0
    result = {
        "calculation_valid": calc_valid,
        "maximum_wave_height": max_wave_height
    }
    return result


def validate_request_params(lat: float, lng: float):
    """
    Check if the lat and lng is within the available ranges.

    Available ranges: (Defined as min and max +- 0.5 degrees)
        - lat [-60.5, 70.5]
        - lng [-180.5, 180]
    """
    return is_float_within_bounds(lat, -60.5, 70.5) and is_float_within_bounds(lng, -180.5, 180)


def is_float_within_bounds(number: float, lower_bound: float, upper_bound: float) -> bool:
    return number > lower_bound and number < upper_bound


def calculate_approx_max_wave_height(lat: float, lng: float) -> tuple[bool, float]:
    """
    Calculate the approx max wave height.

    Finds the nearest point that we have data for and calculates the maximum height of that point.

    Returns calc_valid signifying whether the calculated max height can be assumed correct or not.
    """
    hmax_at_point = hmax_data_array.sel(
        {'longitude': lng, 'latitude': lat}, method="nearest")
    max_hmax_at_point = hmax_at_point.max()
    if math.isnan(max_hmax_at_point.item()):
        return False, 0
    return True, max_hmax_at_point.item()
