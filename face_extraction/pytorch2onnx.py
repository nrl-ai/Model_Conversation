import torch
import argparse
import importlib
import torch.onnx


def load_model(network):
    module = importlib.import_module("iresnet")
    model_class = getattr(module, network)
    return model_class()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PyTorch ArcFace To ONNX Model")
    parser.add_argument(
        "--network", type=str, default="iresnet18", help="backbone network"
    )
    parser.add_argument("--weight", type=str, default="")
    parser.add_argument("--device", type=str, default="cpu", help="device to run model")
    parser.add_argument("--batch_size", type=int, default=1, help="batch size")
    parser.add_argument("--onnx_name", default="model.onnx", help="onnx model name")

    args = parser.parse_args()

    device = torch.device(args.device)

    network = args.network
    weight = torch.load(args.weight, map_location=device)

    model = load_model(network)
    model.load_state_dict(weight)
    model.to(device).eval()

    x = torch.randn(args.batch_size, 3, 112, 112).to(device)
    torch_out = model(x)

    torch.onnx.export(
        model,
        x,
        args.onnx_name,
        export_params=True,
        opset_version=10,
        do_constant_folding=True,
        input_names=["input"],
        output_names=["output"],
        dynamic_axes={
            "input": {0: "batch_size"},
            "output": {0: "batch_size"},
        },
    )
