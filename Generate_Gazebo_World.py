import shutil

Input_World = open("default_world.world", "r") # Load in the world file
number_of_drones = int(input("number of drones: "))

Input_World_Lines = Input_World.readlines()

outputfile = open('outputworld.world', 'a') # Create output file

src = 'BaseDrone' # folder containing the drone to be copied

for i in range(0, len(Input_World_Lines)):
    outputfile.write(Input_World_Lines[i])
    if i == Input_World_Lines.index("  </world>\n") - 1:
        #print(i)
        for drone in range(1, number_of_drones + 1):
            outputfile.write('    <model name="drone{}">\n'.format(drone))
            outputfile.write('      <pose> {} 0 0 0 0 0</pose>\n'.format((drone * 2)))
            outputfile.write('      <include>\n')
            outputfile.write('        <uri>model://drone{}</uri>\n'.format(drone))
            outputfile.write('      </include>\n')
            outputfile.write('    </model>\n')
outputfile.close()


for drone in range(1, number_of_drones + 1):
    dst = 'Output\drone{}'.format(drone)
    try:
        shutil.copytree(src,dst)
    except shutil.Error as exc:
        # handle any exception that might occur
        print("Got exception {} while copying {} to {}".format(exc, src, dst))
    print("copied")


count = 1
for port in range(9002, 9002 + (number_of_drones * 10), 10):
    default_iris_models = open("default_iris_models.txt")
    default_ardupilot_plugin = open("default_ardupilot_plugin.txt")
    default_iris_models_array = default_iris_models.readlines()
    default_ardupilot_plugin_array = default_ardupilot_plugin.readlines()

    default_ardupilot_plugin_array[2] = str('      <fdm_port_in>{}</fdm_port_in>\n'.format(port))
    default_ardupilot_plugin_array[3] = str('      <fdm_port_out>{}</fdm_port_out>\n'.format(port + 1))
    print(default_ardupilot_plugin_array)
    model = open('Output\drone{}\model.sdf'.format(count), 'a')

    for line in default_iris_models_array[:-5]: # Write back the majority of the model files
        model.write(line)
    for line in default_ardupilot_plugin_array: # Inject the ardupilot plugin with ports setup
        model.write(line)
    for line in default_iris_models_array[-5:]: # Write the closing statements
        model.write(line)

    count += 1