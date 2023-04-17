import xml.etree.cElementTree as ET

root = ET.Element("robot")

while True:
    while True:
        link_name = input("what will be the link name, link name should start with link_ : ")
        if link_name.startswith("link_"):
            while True:
                shapeChosen = input('''What shape you want to use:
                1 = Solid sphere
                2 = Solid cuboid
                3 = Solid cylinder ''')
                
                if shapeChosen not in ["1", "2", "3"]:
                    print("Not a valid answer, try again.")
                    continue
                else:
                    break
            break
        else:
            print("Not a valid answer, try again.")
            continue
        
    if shapeChosen == "1":
        print("you choosed Solid sphere, give: mass, radius")
        while True:
            try:
                mass = float(input("now give, mass as decimal number: "))
                radius = float(input("now give, radius as decimal number: "))
                    
                inertia_value = (2/5) * mass * radius**2
                    
                link = ET.Element("link", {"name": link_name})
                inertial = ET.SubElement(link, "inertial")
                mass = ET.SubElement(inertial, "mass", {"value": str(mass)})
                inertia = ET.SubElement(inertial, "inertia", {"ixx": str(inertia_value),"ixy": "0.0", "ixz": "0.0", "iyy": str(inertia_value),"iyz": "0.0","izz": str(inertia_value)})
                visual = ET.SubElement(link, "visual")
                geometry = ET.SubElement(visual, "geometry")
                sphere = ET.SubElement(geometry, "sphere", {"radius": str(radius)})
                collision = ET.SubElement(link, "collision")
                geometry_v2 = ET.SubElement(collision, "geometry")
                sphere_v2 = ET.SubElement(geometry_v2, "sphere", {"radius": str(radius)})
                
                root.append(link)
                
                break
            except ValueError:
                print("Not a valid answer, try again.")
            
    elif shapeChosen == "2":
        print("you choosed Solid cuboid, give: width w, height h, depth d, and mass m")
        while True:
            try:
                mass = float(input("now give, mass as decimal number: "))
                width = float(input("now give, width as decimal number: "))
                height = float(input("now give, height as decimal number: "))
                depth = float(input("now give, depth as decimal number: "))
                    
                inertia_value_height = (1/12) * mass * (width**2 + depth**2)
                inertia_value_width = (1/12) * mass * (depth**2 + height**2)
                inertia_value_depth = (1/12) * mass * (width**2 + height**2)
                
                link = ET.Element("link", {"name": link_name})
                inertial = ET.SubElement(link, "inertial")
                mass = ET.SubElement(inertial, "mass", {"value": str(mass)})
                inertia = ET.SubElement(inertial, "inertia", {"ixx": str(inertia_value_width),"ixy": "0.0", "ixz": "0.0", "iyy": str(inertia_value_depth),"iyz": "0.0","izz": str(inertia_value_height)})
                visual = ET.SubElement(link, "visual")
                geometry = ET.SubElement(visual, "geometry")
                box = ET.SubElement(geometry, "box", {"size": f"{depth} {width} {height}"})
                collision = ET.SubElement(link, "collision")
                geometry_v2 = ET.SubElement(collision, "geometry")
                box_v2 = ET.SubElement(geometry_v2, "box", {"size": f"{depth} {width} {height}"})
                
                root.append(link)
                
                break
            except ValueError:
                print("Not a valid answer, try again.")        
            
    elif shapeChosen == "3":
        print("you choosed Solid cylinder, give: radius r, height h and mass m")
        while True:
            try:
                mass = float(input("now give, mass as decimal number: "))
                radius = float(input("now give, radius as decimal number: "))
                height = float(input("now give, height as decimal number: "))
                
                inertia_value = (1/12) * mass * (3 * radius**2 + height**2)
                inertia_value_v2 = (1/2) * mass * radius**2
                
                link = ET.Element("link", {"name": link_name})
                inertial = ET.SubElement(link, "inertial")
                mass = ET.SubElement(inertial, "mass", {"value": str(mass)})
                inertia = ET.SubElement(inertial, "inertia", {"ixx": str(inertia_value),"ixy": "0.0", "ixz": "0.0", "iyy": str(inertia_value),"iyz": "0.0","izz": str(inertia_value_v2)})
                visual = ET.SubElement(link, "visual")
                geometry = ET.SubElement(visual, "geometry")
                cylinder = ET.SubElement(geometry, "cylinder", {"lenght": str(height), "radius": str(radius)})
                collision = ET.SubElement(link, "collision")
                geometry_v2 = ET.SubElement(collision, "geometry")
                cylinder_v2 = ET.SubElement(geometry_v2, "cylinder", {"lenght": str(height), "radius": str(radius)})
                
                root.append(link)
                
                break
            except ValueError:
                print("Not a valid answer, try again.")
        
    else:
        print("Not a valid answer, try again.")
        
    while True:    
        add_another = input("Do you want to quit, then answer yes if you want to continue answer no ")
        if add_another.lower() == "yes":
            file_name = input("give a filename where to save, use .xml ending for filename: ")
            if not file_name.endswith(".xml"):
                print("Not a valid filename. Please use .xml ending.")
                continue
            
            tree = ET.ElementTree(root)
            tree.write(file_name)
            
            break
        elif add_another.lower() == "no":
            break
        else:
            print("Not a valid answer, try again.")
            continue
    if add_another == "yes":
        break
    else:
        continue