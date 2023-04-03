from osgeo import gdal

# #Para a imagem de satélite

sentinel_image = gdal.Open('')
gt = sentinel_image.GetGeoTransform()

# get coordinates of upper left corner
xmin = gt[0]
ymax = gt[3]
res = gt[1]

# determine total length of raster
xlen = res * round((sentinel_image.RasterXSize//512)*512)
ylen = res * round((sentinel_image.RasterYSize//512)*512)

# number of tiles in x and y direction
xdiv = round((sentinel_image.RasterXSize//512)*512 / 512)
ydiv = round((sentinel_image.RasterYSize//512)*512 / 512)

# size of a single tile
xsize = xlen/xdiv
ysize = ylen/ydiv

# create lists of x and y coordinates
xsteps = [xmin + xsize * i for i in range(xdiv+1)]
ysteps = [ymax - ysize * i for i in range(ydiv+1)]

# loop over min and max x and y coordinates
for i in range(xdiv):
    for j in range(ydiv):
        xmin = xsteps[i]
        xmax = xsteps[i+1]
        ymax = ysteps[j]
        ymin = ysteps[j+1]

        # gdal translate to subset the input raster
        gdal.Translate("sentinel_image_patch"+str(i)+"-"+str(j)+".tif", sentinel_image, projWin = (xmin, ymax, xmax, ymin), xRes = res, yRes = -res)
 
# close the open dataset!!!
sentinel_image_mask = None


#Para a máscara da iamgem de satélite

sentinel_image_mask = gdal.Open('')
gt = sentinel_image_mask.GetGeoTransform()

# get coordinates of upper left corner
xmin = gt[0]
ymax = gt[3]
res = gt[1]

# determine total length of raster
xlen = res * round((sentinel_image_mask.RasterXSize//512)*512)
ylen = res * round((sentinel_image_mask.RasterYSize//512)*512)

# number of tiles in x and y direction
xdiv = round((sentinel_image_mask.RasterXSize//512)*512 / 512)
ydiv = round((sentinel_image_mask.RasterYSize//512)*512 / 512)

# size of a single tile
xsize = xlen/xdiv
ysize = ylen/ydiv

# create lists of x and y coordinates
xsteps = [xmin + xsize * i for i in range(xdiv+1)]
ysteps = [ymax - ysize * i for i in range(ydiv+1)]

# loop over min and max x and y coordinates
for i in range(xdiv):
    for j in range(ydiv):
        xmin = xsteps[i]
        xmax = xsteps[i+1]
        ymax = ysteps[j]
        ymin = ysteps[j+1]

        # gdal translate to subset the input raster
        gdal.Translate("sentinel_image_patch"+str(i)+"-"+str(j)+"_mask"+".tif", sentinel_image_mask, projWin = (xmin, ymax, xmax, ymin), xRes = res, yRes = -res)
 
# close the open dataset!!!
sentinel_image_mask = None