import unittest
from unittest.mock import MagicMock
import rclpy
from turtle_logger.turtle_logger import TurtleLogger
from turtlesim.msg import Pose

class TestTurtleLogger(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        rclpy.init()

    @classmethod
    def tearDownClass(cls):
        rclpy.shutdown()

    def setUp(self):
        self.node = TurtleLogger()
        self.node.get_logger = MagicMock()

    def tearDown(self):
        self.node.destroy_node()

    def test_pose_callback_sets_pose(self):
        pose = Pose()
        pose.x = 5.0
        pose.y = 5.0
        pose.theta = 1.0
        self.node.pose_callback(pose)
        self.assertEqual(self.node.current_pose, pose)

    def test_log_position_info(self):
        pose = Pose(x=5.0, y=5.0, theta=1.0)
        self.node.current_pose = pose
        self.node.log_position()
        self.node.get_logger().info.assert_called_once()

    def test_log_position_warn(self):
        pose = Pose(x=10.2, y=5.0, theta=1.0)
        self.node.current_pose = pose
        self.node.log_position()
        self.node.get_logger().warn.assert_called_once()

    def test_log_position_error(self):
        pose = Pose(x=10.6, y=0.4, theta=1.0)
        self.node.current_pose = pose
        self.node.log_position()
        self.node.get_logger().error.assert_called_once()

if __name__ == '__main__':
    unittest.main()
