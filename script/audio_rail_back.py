#!/usr/bin/env python

import rospy
import sys

from sound_play.libsoundplay import SoundClient


def play_repeat():
    soundhandle = SoundClient()
    rospy.sleep(0.5)

    sound_beep = soundhandle.waveSound("/root/farmingo_ws/src/farmingo/play_audio/wav/tesla_seatbelt.wav")
    sound_beep.stop()
    sound_beep.play()
    sound_beep.repeat()
    #rospy.loginfo('first beep')
    #rospy.sleep(1)
    for i in range(100):
        #sound_beep.repeat()
        #rospy.loginfo('repeat beep: {}'.format(i))
        if rospy.is_shutdown():
            break
        rospy.sleep(1)


if __name__ == '__main__':
    rospy.init_node('repeat_test')
    play_repeat()
    rospy.spin()