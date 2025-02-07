import dataclasses
import json

import pygame

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

PLAYER_RADIUS = 20
PLAYER_SPEED = 200
PLAYER_TURN_SPEED = 300
PLAYER_SHOOT_COOLDOWN = 0.3
PLAYER_SHOOT_SPEED = 500
SHOT_RADIUS = 5


# Globals
@dataclasses.dataclass
class _InputMap:
    forward: list[int]
    backward: list[int]
    left: list[int]
    right: list[int]
    shoot: list[int]

    @staticmethod
    def is_action(action_keys: list[int], active_keys: list[bool]) -> bool:
        return any(active_keys[action_key] for action_key in action_keys)

    def is_forward(self, active_keys: list[bool]) -> bool:
        return self.is_action(self.forward, active_keys)

    def is_backward(self, active_keys: list[bool]) -> bool:
        return self.is_action(self.backward, active_keys)

    def is_left(self, active_keys: list[bool]) -> bool:
        return self.is_action(self.left, active_keys)

    def is_right(self, active_keys: list[bool]) -> bool:
        return self.is_action(self.right, active_keys)

    def is_shoot(self, active_keys: list[bool]) -> bool:
        return self.is_action(self.shoot, active_keys)

    @classmethod
    def load_from_file(cls, filepath: str) -> "_InputMap":
        with open(filepath) as file:
            data = json.load(file)

        get_key = lambda key_name: getattr(pygame, key_name)

        try:
            return cls(
                forward=list(map(get_key, data["forward"])),
                backward=list(map(get_key, data["backward"])),
                left=list(map(get_key, data["left"])),
                right=list(map(get_key, data["right"])),
                shoot=list(map(get_key, data["shoot"])),
            )
        except KeyError as e:
            print(f"No input for {e} configured! Game is unplayable!")
            exit(1)


InputMap = _InputMap.load_from_file("config.json")
