'''
This is the main program. 
You should read the packaging.txt in the data folder.
Each line contains one package description. 
You should parse the package description using parse_packaging()
print the total number of items in the package using calc_total_units()
along with the unit using get_unit()
place each package in a list and save in JSON format.

Example:

    INPUT (example data/packaging.txt file):
    
    12 eggs in 1 carton
    6 bars in 1 pack / 12 packs in 1 carton

    OUTPUT: (print to console)

    12 eggs in 1 carton => total units: 12 eggs
    6 bars in 1 pack / 12 packs in 1 carton => total units: 72 bars

    OUTPUT (example data/packaging.json file):
    [
        [{ 'eggs' : 12}, {'carton' : 1}],
        [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}],
    ]    
'''

def parse_packaging(packaging_data: str) -> list[dict]:

    result = []
    layers = packaging_data.split(" in ")

    for layer in layers:
        words = layer.split() 
        number = int(words[0]) 
        name = words[1]
        result.append({name: number})

    return result



def calc_total_units(package: list[dict]) -> int:

    total = 1 

    for item in package:
        for key in item: 
            total *= item[key] 

    return total 


def get_unit(package: list[dict]) -> str:

    if not package:
        return "" 

    first_item = package[0]
    return list(first_item.keys())[0] 


# This will only run from here, not when imported
# # Use this for testing / debugging cases with the debugger
if __name__ == '__main__':
    
    text = "25 balls in 1 bucket / 4 buckets in 1 bin"
    package = parse_packaging(text)
    print(package)

    package_total = calc_total_units(package)
    unit = get_unit(package)
    print(f"{package_total} {unit} total")