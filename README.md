# Model_Conversation

## Face Extraction
**Reference** [Link](https://github.com/deepinsight/insightface/tree/master/recognition/arcface_torch)

**Steps**
- Download model [Link](https://github.com/deepinsight/insightface/tree/master/recognition/arcface_torch)
- Convert Pytorch to ONNX [Example](face_extraction/example_convertion.sh)
- Simplifier ONNX [Example](face_extraction/onnx_simplifier.sh)
- Convert ONNX to NCNN [Example](face_extraction/onnx2ncnn.sh)
