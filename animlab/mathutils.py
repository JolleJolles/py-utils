
# coding: utf-8

# In[ ]:


import numpy as np

def uneven(value):
    
    """ Calculates the closest uneven value equal to or lower than provided """
    
    value = value + (value - 1) if value > 0 else 1
    
    return value


def points_to_vec(pt1, pt2):
    
    vx = pt2[0] - pt1[0]
    vy = pt1[1] - pt2[1]
    
    return vx, vy


def angle_to_vec(angle):
    
    vx = np.round(np.sin(np.radians(angle)), 3)
    vy = np.round(np.cos(np.radians(angle)), 3)
    
    return vx, vy


def points_to_angle(pt1, pt2 = None):
    
    """ Returns the angle of a vector based on eiher one or two points"""
    
    vx, vy = pt1 if pt2 is None else vec_from_points(pt, pt2)
    angle = np.round(np.arctan2(vx, vy) * 180 / np.pi,2)

    return angle


def points_to_dist(pt1, pt2):
    
    if None in pt1 or None in pt2:
        vel = None
    else:
        vx, vy = vec_from_points(pt1, pt2)
        vel = np.linalg.norm([(vx, vy)])
    
    return dist


def diff_series(series, period = 1):
    
    series2 = series.shift(periods = -period)

    return series2 - series


def distoline(point, line):
    
    """
    Calculate the distance between a point and a line segment
    
    Explanation
    ----------
    To calculate the closest distance to a line segment, we first need to check
    if the point projects onto the line segment.  If it does, then we calculate
    the orthogonal distance from the point to the line. If the point does not 
    project to the line segment, we calculate the distance to both endpoints 
    and take the shortest distance.
    
    Returns
    -------
    segment_dist : the perpendicular distance to the theoretical infinite line
    (x_seg, y_seg) : the relative x and y coordinates to the line
    endpoint_dist : minimum distance to the end point on the line
    
    """

    # unit vector
    unit_line = line[1] - line[0]
    norm_unit_line = unit_line / np.linalg.norm(unit_line)

    # compute the perpendicular distance to the theoretical infinite line
    segment_dist = (np.linalg.norm(np.cross(line[1] - line[0], line[0] - point)) / np.linalg.norm(unit_line))
    diff = ((norm_unit_line[0] * (point[0] - line[0][0])) + (norm_unit_line[1] * (point[1] - line[0][1])))
    x_seg = (norm_unit_line[0] * diff) + line[0][0]
    y_seg = (norm_unit_line[1] * diff) + line[0][1]
    
    coords = (x_seg, y_seg)
    distance = segment_dist
    
    linept1dis = np.linalg.norm(line[0] - point)
    linept2dis = np.linalg.norm(line[1] - point)
    endpoint_dist = min(linept1dis, linept2dis)

    # decide if the intersection point falls on the line segment
    lp1_x = line[0][0]
    lp1_y = line[0][1]
    lp2_x = line[1][0]
    lp2_y = line[1][1]
    is_betw_x = lp1_x <= x_seg <= lp2_x or lp2_x <= x_seg <= lp1_x
    is_betw_y = lp1_y <= y_seg <= lp2_y or lp2_y <= y_seg <= lp1_y

#    if is_betw_x and is_betw_y:
#        coords = (x_seg, y_seg)
#        distance = segment_dist
#    else:
#        # if not, then return the minimum distance to the segment endpoints
#        #coords = (line[0][0],line[0][1]) if linept1dis<=linept2dis else (line[1][0],line[1][1])
#        distance = endpoint_dist
    
    return segment_dist, (x_seg, y_seg), endpoint_dist
