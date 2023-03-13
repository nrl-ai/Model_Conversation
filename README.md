# Model Conversion

## Face Extraction
**Reference** [Link](https://github.com/deepinsight/insightface/tree/master/recognition/arcface_torch)

**Steps**
- Download model [Link](https://github.com/deepinsight/insightface/tree/master/recognition/arcface_torch)
- Convert Pytorch to ONNX [Example](face_extraction/example_convertion.sh)
- Simplifier ONNX [Example](face_extraction/onnx_simplifier.sh)
- Convert ONNX to NCNN [Example](face_extraction/onnx2ncnn.sh)

## Face Detection
**Reference** [Link](https://github.com/deepinsight/insightface/tree/master/detection/scrfd)

**Steps**
- Install enviroment from [Link](https://github.com/deepinsight/insightface/tree/master/detection/scrfd)
- Download model from [Link](https://github.com/deepinsight/insightface/tree/master/detection/scrfd), **note** model name must have type "*KPS"
- Convert To ONNX [Example](face_detection/scrfd/convert_to_onnx.sh)
- Simplifier ONNX [Example](face_detection/scrfd/onnx_simplifier.sh)
- Convert ONNX to NCNN [Example](face_detection/scrfd/onnx2ncnn.sh)
