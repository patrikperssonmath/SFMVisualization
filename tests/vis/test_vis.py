
#import context

from visualization.vis import visualize_prediction, InteractiveViz, Queue
import numpy as np

def test_visualization():

    points = np.random.rand(10,3).astype(np.float32)
    color = (np.random.rand(10,3)*255.0).astype(np.float32)

    visualize_prediction(points, color, [])

def test_visualization_callback():

    points = np.random.rand(10,3).astype(np.float32)
    color = (np.random.rand(10,3)*255.0).astype(np.float32)

    queue = Queue()

    viz = InteractiveViz(queue, False, None, False)

    keyframe_pose = None
    pointcloud = (points, color)

    viz.start()

    queue.put((pointcloud, keyframe_pose))