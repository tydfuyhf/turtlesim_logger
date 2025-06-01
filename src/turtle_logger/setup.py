from setuptools import find_packages, setup

package_name = 'turtle_logger'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=[
        'setuptools',
        'rclpy',
        'geometry_msgs',
        'turtlesim',
    ],
    zip_safe=True,
    maintainer='park',
    maintainer_email='park@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': [
            'turtle_logger = turtle_logger.turtle_logger:main',
        ],
    },
)

