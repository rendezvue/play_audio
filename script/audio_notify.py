#!/usr/bin/env python

import rospy
import sys
import rospkg
from sound_play.libsoundplay import SoundClient


def play_repeat():
    soundhandle = SoundClient()
    rospy.sleep(0.5)
    rospy.loginfo("Sending stopAll commande every 100 ms.")
    rospy.loginfo("Note: This will not prevent a node that is continuing to issue commands")
    rospy.loginfo("from producing sound.")
    rospy.loginfo("Press Ctrl+C to exit.")

    soundhandle.stopAll()
    rospy.sleep(1)
    
    rospack = rospkg.RosPack()
    wav_path = rospack.get_path('play_audio')

    sound_beep = soundhandle.waveSound(wav_path+"/wav/WindowsLogon.wav")
    sound_beep.play()
if __name__ == '__main__':
    rospy.init_node('repeat_test')
    play_repeat()
    rospy.spin()
