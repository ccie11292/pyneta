from ciscoconfparse import CiscoConfParse

# When feeding config directly - CiscoConfParse requires a list
cisco_cfg = CiscoConfParse("lab3-7.txt")
bgp_neighbors = cisco_cfg.find_objects_w_parents(
    parentspec=r"^router bgp", childspec=r"^\s+neighbor"
)

bgp_neighbor_list = []

for neigh in bgp_neighbors:
    remote_as = neigh.re_search_children(r"\s+remote-as")[0].text
    remote_as = remote_as.split()
    remote_as = remote_as[1]
    #print(remote_as)
    
    bgp_neigh = neigh.text
    bgp_neigh = bgp_neigh.split()
    bgp_neigh = bgp_neigh[1]
    #print (bgp_neigh)

    remote_as = neigh.re_search_children(r"\s+remote-as")[0].text
    remote_as = remote_as.split()
    remote_as = remote_as[1]
    #print(remote_as)

    bgp_data = []
    #print(bgp_data)
    bgp_data.append(bgp_neigh)
    #print(bgp_data)

    bgp_data.append(remote_as)
    #print(bgp_data)

    bgp_neighbor_list.append(tuple(bgp_data))


print(bgp_neighbor_list)
