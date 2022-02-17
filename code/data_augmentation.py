from imgaug import augmenters as iaa
seq = iaa.Sequential([
                iaa.Affine(rotate=(-25, 25)),  # Rotation des images
                iaa.AdditiveGaussianNoise(scale=(15, 60)),  # Bruit
                iaa.Crop(percent=(0, 0.2)),  # Retire des lignes/colonnes
                iaa.Dropout([0.05, 0.2]),  # Enlève des pixels uniformément
                iaa.Sharpen((0.0, 1.0)),  # Augmente les contours
                iaa.ElasticTransformation(alpha=50, sigma=5)  # Bouge les pixels localement
            ], random_order=True)
            segmap = SegmentationMapsOnImage(segmap, shape=image.shape)
