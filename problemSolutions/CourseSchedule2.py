from Solution import Solution
from collections import defaultdict, deque


class CourseSchedule2(Solution):
    """
    There are a total of numCourses courses you have to take, labeled from 0 to
    numCourses -1 . You are given an array prerequisites where prerequisites
    [i]= [a_i, b_i] indicates that you must take course b_i first if you want to
    take course a_i.

        - For example, the pair [0,1], indicates that to take course 0 you have
        to first take course 1 .

    Return the ordering of courses you should take to finish all courses.
    If there are many valid answers, return any of them. If it is impossible to
    finish all courses, return an empty array.
    """

    def __init__(self):
        super().__init__()

    def solution(self, numCourses: int, prerequisites: list[list[int]]) -> None:
        """
        The solution is a direct application of Kahn's algorithm for topological
        sorting.

        Parameters
        ----------
        numCourses : number of courses.

        prerequisites : list of prerequisites.

        Returns
        -------
        updates answer to a list of the courses to take in order.
        """

        # Prepare the graph
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)

            # Record each node's in-degree
            indegree[dest] = indegree.get(dest, 0) + 1

        # Queue for maintainig list of nodes that have 0 in-degree
        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])

        topological_sorted_order = []

        # Until there are nodes in the Q
        while zero_indegree_queue:
            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)

            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        if len(topological_sorted_order) == numCourses:
            self.setSolution(topological_sorted_order)
        else:
            self.setSolution([])
