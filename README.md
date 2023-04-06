## Running the project

01. Make sure you have a folder structure /home/<user>/ros_ws/src/<project folder>
    - <project folder> is where you'd need to clone the demo_bot project
01. Do `cd` to `ros_ws` directory. you should be inside `ros_ws/` folder
01. Run `source /opt/ros/galactic/setup.bash`
01. Note - galactic is the version of ros distribution. if you are using a different distribution use that
01. Run `colcon build` to build the workspace.
01. Run `source install/setup.bash` to export the local dependencies
01. Run `ros2 launch demo_bot launch_gaz.launch.py` to launch the project 


