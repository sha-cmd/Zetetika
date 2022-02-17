for pic_num in range(len(layer_list)):
    # pic_num : boucle de chacun de nos fichiers json à 8 catégories
    dfl = pd.read_json(layer_list[pic_num])
    h = dfl.at[0, 'imgHeight']
    w = dfl.at[0, 'imgWidth']
    img_mask = np.zeros(np.hstack((h, w)), dtype='uint8')
    for poly_num in range(len(dfl)):
        label = dfl.at[poly_num, 'objects']['label']
        poly = np.array([dfl.at[poly_num, 'objects']['polygon']])
        img_mask = cv2.fillPoly(img_mask, poly, dict_label_clr[label])
