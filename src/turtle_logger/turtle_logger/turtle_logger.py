import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class TurtleLogger(Node):
    def __init__(self):
        super().__init__('turtle_logger')
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )
        self.timer = self.create_timer(1.0, self.log_position)  # 1초마다 로그 출력
        self.current_pose = None
        self.get_logger().info('Turtle Logger 노드가 시작되었습니다!')

    def pose_callback(self, msg):
        self.current_pose = msg

    def log_position(self):
        if self.current_pose:
            x, y = self.current_pose.x, self.current_pose.y
            theta = self.current_pose.theta

            # 화면 끝에 가까운지 확인
            if x < 1.0 or x > 10.0 or y < 1.0 or y > 10.0:
                if x <= 0.5 or x >= 10.5 or y <= 0.5 or y >= 10.5:
                    self.get_logger().error(f'터틀이 화면을 벗어나려고 합니다! (x: {x:.2f}, y: {y:.2f}, θ: {theta:.2f})')
                else:
                    self.get_logger().warn(f'터틀이 화면 가장자리에 가깝습니다. (x: {x:.2f}, y: {y:.2f}, θ: {theta:.2f})')
            else:
                self.get_logger().info(f'터틀 위치 - x: {x:.2f}, y: {y:.2f}, θ: {theta:.2f}')

def main(args=None):
    rclpy.init(args=args)
    turtle_logger = TurtleLogger()
    try:
        rclpy.spin(turtle_logger)
    except KeyboardInterrupt:
        pass
    finally:
        turtle_logger.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

