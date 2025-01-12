def trap(height) -> int:
        TRAPPED_WATER = 0

        height_list = height

        left_boundary = [0] * (len(height_list))
        right_boundary = [0] * (len(height_list))

        for i in range(len(height_list)):
            last_index = len(height_list) - 1
            j = last_index - i

            # Calculating the left boundary
            if i == 0:
                left_boundary[i] = height_list[i]

            else:
                left_boundary[i] = height_list[i] if (height_list[i] >= left_boundary[i - 1]) else left_boundary[i - 1]

            # Calculating the right boundary

            if j == last_index:

                right_boundary[j] = height_list[j]

            else:

                right_boundary[j] = height_list[j] if (height_list[j] >= right_boundary[j + 1]) else right_boundary[
                    j + 1]

            # Calculating Trapper water

        for i in range(len(height_list)):
            TRAPPED_WATER += (right_boundary[i] if (right_boundary[i] <= left_boundary[i]) else left_boundary[i]) - \
                             height_list[i]

        # print(TRAPPED_WATER)
        return TRAPPED_WATER

trap([0,1,0,2,1,0,1,3,2,1,2,1])