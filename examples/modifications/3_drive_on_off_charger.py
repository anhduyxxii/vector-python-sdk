#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tell Vector to drive on and off the charger.
"""
import time
import anki_vector


def main():
    args = anki_vector.util.parse_command_args()

    with anki_vector.Robot(args.serial) as robot:
        print("Vector is now Docked") if robot.status.is_on_charger else print("Vector is now off Dock")
        time.sleep(1)
        print("Driving Vector off Dock...")
        robot.behavior.drive_off_charger()
        print("Vector is now Docked") if robot.status.is_on_charger else print("Vector is now off Dock")
        time.sleep(2)

        print("Driving Vector onto Dock...")
        robot.behavior.drive_on_charger()
        print("Vector is now Docked") if robot.status.is_on_charger else print("Vector is now off Dock")
        time.sleep(2)

        battery_levels = {1: "LOW", 2: "NOMINAL", 3: "FULL"}
        battery_state = robot.get_battery_state()
        if battery_state:
            print("Battery: {0}(V) - {1} {2}".format(round(battery_state.battery_volts, 2), battery_levels[battery_state.battery_level], "(Charging...)" if robot.status.is_charging else ""))

        print("End Task")

if __name__ == '__main__':
    main()
