#!/usr/bin/env python
from __future__ import print_function

import sys
import rospy
import actionlib
from geometry_msgs.msg import Point
from geometry_msgs.msg import PoseStamped
from geometry_msgs.msg import Pose
from std_msgs.msg import Header

from move_base_msgs.msg import MoveBaseAction
# from move_base_msgs.msg import MoveBaseActionClient
from move_base_msgs.msg import MoveBaseGoal

from poi_name_locator.srv import PoiNameLocator
from poi_name_locator.srv import PoiNameLocatorRequest
from poi_name_locator.srv import PoiNameLocatorResponse
from poi_name_locator.srv import PoiNames
from poi_name_locator.srv import PoiNamesRequest
from poi_name_locator.srv import PoiNamesResponse


# A simple demonstration of using poi_name_locator to lookup two points, and then patrol back and forth
# between those points, indefinitely.
class Patrol:
    def __init__(self):
        rospy.init_node('doors_patrol')

        rospy.loginfo('waiting for service poi_names')
        rospy.wait_for_service('poi_names')
        rospy.loginfo('waiting for service poi_names finished')

        self.poi_name_locator_callable = rospy.ServiceProxy(
            'poi_name_locator', PoiNameLocator
        )  # type: callable(PoiNamesRequest) -> PoiNamesResponse
	
	self.poi_names_callable = rospy.ServiceProxy('poi_names', PoiNames)

        self.move_base_action_client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.move_base_action_client.wait_for_server()

    def lookup(self, poi_name):  # type: (str) -> Point
        request = PoiNameLocatorRequest(poi_name)

        # response cannot be None. If server tries to return None, a rospy.ServiceException will raise here.
        response = self.poi_name_locator_callable(request)  # type: PoiNameLocatorResponse

        return response.position

    def patrol(self, poi1):  # type: (str, str) -> None
        point1 = self.lookup(poi1)  # type: Point

        goal = MoveBaseGoal()
        target_pose = goal.target_pose  # type: PoseStamped

        header = target_pose.header  # type: Header
        header.frame_id = "/map"

        pose = target_pose.pose  # type: Pose

        # pose.orientation  by default is just a bunch of 0's, which is not valid because the length of the
        # vector is 0. Length of vector must be 1, and for map navigation, z-axis must be vertical, so by setting
        # w = 1, it's the same as yaw = 0
        pose.orientation.w = 1

        while not rospy.is_shutdown():
            ########### Drive to poi1
            rospy.loginfo('drive to {}'.format(poi1))

            pose.position = point1
            header.stamp = rospy.Time.now()

            self.move_base_action_client.send_goal(goal)
            self.move_base_action_client.wait_for_result()

            rospy.loginfo('arrived, now waiting 10 sec')
            for i in range(100):
                if rospy.is_shutdown():
                    return
                rospy.sleep(0.1)


if __name__ == "__main__":
    patrol = Patrol()

   
    relist = PoiNamesResponse()

    for x in range(34)
	patrol.Patrol(retlist[x])
	rospy.sleep(100)



