dijkstra(start, end, n, K, A, B, C, gas_stations):
    Create a priority queue Q
    Initialize distances dist to infinity for all nodes
    Set dist[start] = 0
    Initialize tank to K and cost to 0

    Q.add(start)

    while Q is not empty:
        current = Q.poll()
        x, y = current

        if current == end:
            return dist[end]

        # check if we need to refill tank
        if tank == 0:
            cost += A
            tank = K

        # check if there's a gas station on this intersection
        if (x, y) in gas_stations:
            Q.add((x, y))

        # check if we can move right and add to queue
        if x < n:
            next_node = (x+1, y)
            next_dist = 1 + cost
            if next_node in gas_stations:
                next_dist += C
            if next_node not in dist or next_dist < dist[next_node]:
                dist[next_node] = next_dist
                Q.add(next_node)
                tank -= 1

        # check if we can move up and add to queue
        if y < n:
            next_node = (x, y+1)
            next_dist = 1 + cost
            if next_node in gas_stations:
                next_dist += C
            if next_node not in dist or next_dist < dist[next_node]:
                dist[next_node] = next_dist
                Q.add(next_node)
                tank -= 1

        # check if we can move left and add to queue
        if x > 0:
            next_node = (x-1, y)
            next_dist = 1 + cost
            if next_node in gas_stations:
                next_dist += C + B
            elif (x-1, y) in gas_stations:
                next_dist += A + C
            else:
                next_dist += B
            if next_node not in dist or next_dist < dist[next_node]:
                dist[next_node] = next_dist
                Q.add(next_node)
                tank -= 1

        # check if we can move down and add to queue
        if y > 0:
            next_node = (x, y-1)
            next_dist = 1 + cost
            if next_node in gas_stations:
                next_dist += C + B
            elif (x, y-1) in gas_stations:
                next_dist += A + C
            else:
                next_dist += B
            if next_node not in dist or next_dist < dist[next_node]:
                dist[next_node] = next_dist
                Q.add(next_node)
                tank -= 1

    # no path found
    return -1
