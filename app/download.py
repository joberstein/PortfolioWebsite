from flask import request, Blueprint, send_file
download_file = Blueprint("download_file", __name__)


@download_file.route("/download", methods=["GET"])
def download():
    file_path = request.args.get("file_path")
    download_name = request.args.get("download_name")
    return send_file(file_path, as_attachment=True, attachment_filename=download_name)