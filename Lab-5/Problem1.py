resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 0],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]


def display_resources(resources):
    if len(resources) == 0:
        print("No resources to show.")
        return

    for resource in resources:
        if resource[3] < 0:
            print(resource[1], "has an invalid quantity:", resource[3])
        else:
            print("ID:", resource[0], "| Name:", resource[1], "| Category:", resource[2], "| Quantity:", resource[3])


def search_by_category(resources, category):
    found = False
    for resource in resources:
        if resource[2].lower() == category.lower():
            print(resource[1], "-", resource[3], "available")
            found = True

    if not found:
        print("No resources in category:", category)


def find_unavailable(resources):
    found = False
    for resource in resources:
        if resource[3] == 0:
            print(resource[1], "is unavailable")
            found = True

    if not found:
        print("All resources are available.")


def find_resource(resources, resource_id):
    for resource in resources:
        if resource[0] == resource_id:
            return resource
    return None


# Testing
print("--- All resources ---")
display_resources(resources)

print("--- Electronics ---")
search_by_category(resources, "Electronics")

print("--- Unavailable ---")
find_unavailable(resources)

print("--- Unknown ID 999 ---")
print(find_resource(resources, 999))

print("--- Negative quantity ---")
display_resources([[106, "Printer", "Office", -3]])

print("--- Empty list ---")
display_resources([])
