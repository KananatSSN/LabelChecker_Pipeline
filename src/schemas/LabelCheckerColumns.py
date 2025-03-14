import pandas as pd
import pyarrow as pa

column_name_types = {
    "Name": pd.ArrowDtype(pa.string()),
    "AbdArea": pd.ArrowDtype(pa.float32()),
    "FilledArea": pd.ArrowDtype(pa.float32()),
    "AspectRatio": pd.ArrowDtype(pa.float32()),
    "AvgBlue": pd.ArrowDtype(pa.float32()),
    "AvgGreen": pd.ArrowDtype(pa.float32()),
    "AvgRed": pd.ArrowDtype(pa.float32()),
    "BiovolumeCylinder": pd.ArrowDtype(pa.float32()),
    "BiovolumePSpheroid": pd.ArrowDtype(pa.float32()),
    "BiovolumeSphere": pd.ArrowDtype(pa.float32()),
    "CalConst": pd.ArrowDtype(pa.float32()),
    "CalImage": pd.ArrowDtype(pa.uint64()),
    "Ch1Area": pd.ArrowDtype(pa.float32()),
    "Ch1Peak": pd.ArrowDtype(pa.float32()),
    "Ch1Width": pd.ArrowDtype(pa.float32()),
    "Ch2Area": pd.ArrowDtype(pa.float32()),
    "Ch2Peak": pd.ArrowDtype(pa.float32()),
    "Ch2Width": pd.ArrowDtype(pa.float32()),
    "Ch2Ch1Ratio": pd.ArrowDtype(pa.float32()),
    "CircleFit": pd.ArrowDtype(pa.float32()),
    "Circularity": pd.ArrowDtype(pa.float32()),
    "CircularityHu": pd.ArrowDtype(pa.float32()),
    "CollageFile": pd.ArrowDtype(pa.string()),
    "Compactness": pd.ArrowDtype(pa.float32()),
    "ConvexPerimeter": pd.ArrowDtype(pa.float32()),
    "Convexity": pd.ArrowDtype(pa.float32()),
    "Date": "Datetime64[pyarrow]",
    "AbdDiameter": pd.ArrowDtype(pa.float32()),
    "EsdDiameter": pd.ArrowDtype(pa.float32()),
    "FdDiameter": pd.ArrowDtype(pa.float32()),
    "EdgeGradient": pd.ArrowDtype(pa.float32()),
    "ElapsedTime": pd.ArrowDtype(pa.float32()),
    "Elongation": pd.ArrowDtype(pa.float32()),
    "FeretMaxAngle": pd.ArrowDtype(pa.float32()),
    "FeretMinAngle": pd.ArrowDtype(pa.float32()),
    "FiberCurl": pd.ArrowDtype(pa.float32()),
    "FiberStraightness": pd.ArrowDtype(pa.float32()),
    "FilterScore": pd.ArrowDtype(pa.float32()),
    "GeodesicAspectRatio": pd.ArrowDtype(pa.float32()),
    "GeodesicLength": pd.ArrowDtype(pa.float32()),
    "GeodesicThickness": pd.ArrowDtype(pa.float32()),
    "GroupId": pd.ArrowDtype(pa.uint64()),
    "Id": pd.ArrowDtype(pa.uint64()),
    "ImageFilename": pd.ArrowDtype(pa.string()),
    "ImageX": pd.ArrowDtype(pa.uint64()),
    "ImageY": pd.ArrowDtype(pa.uint64()),
    "ImageH": pd.ArrowDtype(pa.uint64()),
    "ImageW": pd.ArrowDtype(pa.uint64()),
    "Intensity": pd.ArrowDtype(pa.float32()),
    "Length": pd.ArrowDtype(pa.float32()),
    "Ppc": pd.ArrowDtype(pa.uint64()),
    "Perimeter": pd.ArrowDtype(pa.float32()),
    "RatioBlueGreen": pd.ArrowDtype(pa.float32()),
    "RatioRedBlue": pd.ArrowDtype(pa.float32()),
    "RatioRedGreen": pd.ArrowDtype(pa.float32()),
    "Roughness": pd.ArrowDtype(pa.float32()),
    "SigmaIntensity": pd.ArrowDtype(pa.float32()),
    "SrcImage": pd.ArrowDtype(pa.uint64()),
    "SrcX": pd.ArrowDtype(pa.uint64()),
    "SrcY": pd.ArrowDtype(pa.uint64()),
    "SphereComplement": pd.ArrowDtype(pa.uint64()),
    "SphereCount": pd.ArrowDtype(pa.uint64()),
    "SphereUnknown": pd.ArrowDtype(pa.uint64()),
    "SphereVolume": pd.ArrowDtype(pa.float32()),
    "SumIntensity": pd.ArrowDtype(pa.uint64()),
    "Symmetry": pd.ArrowDtype(pa.float32()),
    "Time": "Datetime64[pyarrow]",
    "Timestamp": "Datetime64[pyarrow]",
    "Transparency": pd.ArrowDtype(pa.float32()),
    "Uuid": pd.ArrowDtype(pa.string()),
    "AbdVolume": pd.ArrowDtype(pa.float32()),
    "EsdVolume": pd.ArrowDtype(pa.float32()),
    "Width": pd.ArrowDtype(pa.float32()),
    "BiovolumeHSosik": pd.ArrowDtype(pa.float32()),
    "SurfaceAreaHSosik": pd.ArrowDtype(pa.float32()),
    "Preprocessing": pd.ArrowDtype(pa.string()),
    "PreprocessingTrue": pd.ArrowDtype(pa.string()),
    "ProbabilityScore": pd.ArrowDtype(pa.float32()),
    "LabelPredicted": pd.ArrowDtype(pa.string()),
    "LabelTrue": pd.ArrowDtype(pa.string()),
}
