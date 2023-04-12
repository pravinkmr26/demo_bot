from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from launch_ros.substitutions import FindPackageShare
from os.path import join



def generate_launch_description():


    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

    package_name='demo_bot' 
    
    pkg_sub = get_package_share_directory('demo_bot')
    
    world_path=join(pkg_sub, 'worlds/gazebo_world.world')

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([join(
                    get_package_share_directory(package_name),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    # Include the Gazebo launch file, provided by the gazebo_ros package
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
             launch_arguments={'world': world_path}.items())

    # spawn_entity.py [-h]
    # [spawn_entity.py-4]                        (-file FILE_NAME | -topic TOPIC_NAME | -database ENTITY_NAME | -stdin)
    # [spawn_entity.py-4]                        -entity ENTITY_NAME [-reference_frame REFERENCE_FRAME]
    # [spawn_entity.py-4]                        [-gazebo_namespace GAZEBO_NAMESPACE]
    # [spawn_entity.py-4]                        [-robot_namespace ROBOT_NAMESPACE] [-timeout TIMEOUT]
    # [spawn_entity.py-4]                        [-unpause] [-wait ENTITY_NAME]
    # [spawn_entity.py-4]                        [-spawn_service_timeout TIMEOUT] [-x X] [-y Y] [-z Z]
    # [spawn_entity.py-4]                        [-R R] [-P P] [-Y Y] [-package_to_model] [-b]
    
    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'my_bot'],
                        output='screen')



    # Launch them all!
    return LaunchDescription([
        # ExecuteProcess(
        #     cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so', world_path], 
        #     output='screen'),
        gazebo,
        rsp,
        spawn_entity
    ])
