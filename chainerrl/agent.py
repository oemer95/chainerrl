from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
from future.utils import with_metaclass
standard_library.install_aliases()

from abc import ABCMeta
from abc import abstractmethod


class Agent(with_metaclass(ABCMeta, object)):
    """Abstract agent class.
    """

    @abstractmethod
    def act_and_train(self, obs, reward):
        """
        Select an action for training.

        Returns:
            ~object: action
        """
        raise NotImplementedError()

    @abstractmethod
    def act(self, obs):
        """
        Select an action for evaluation.

        Returns:
            ~object: action
        """
        raise NotImplementedError()

    @abstractmethod
    def stop_episode_and_train(self, state, reward, done=False):
        """
        Observe consequences and prepare for a new episode.

        Returns:
            None
        """
        raise NotImplementedError()

    @abstractmethod
    def stop_episode(self):
        """
        Prepare for a new episode.

        Returns:
            None
        """
        raise NotImplementedError()

    @abstractmethod
    def save(self, dirname):
        """
        Save internal states.
        """
        raise NotImplementedError()

    @abstractmethod
    def load(self, dirname):
        """
        Load internal states.
        """
        raise NotImplementedError()
