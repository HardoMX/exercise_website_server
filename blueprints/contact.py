from flask import Blueprint, render_template, request, redirect, url_for

contact_bp = Blueprint("contact", __name__)


@contact_bp.route("/contact", methods=["GET"])
def contact():
    return render_template("contact.html")

@contact_bp.route("/contact/contact_manager", methods=["GET"])
def about_manager():
    return render_template("contact_manager.html", contact_content_entries=about_entries)


@contact_bp.route("/cms/about_manager/create", methods=["POST"])
def add_content():
    # Extract data from the form
    print(request.form)
    title = request.form["heading"]
    imageFilename = request.form["imageFilename"]
    introText = request.form["introText"]
    additionalInfo = request.form["additionalInfo"]
    isActive = "isActive" in request.form

    print(imageFilename)
    # Construct the new content entry
    new_content = {
        "id": len(about_entries) + 1,
        "title": title,
        "imageUrl": url_for("static", filename=f"img/{imageFilename}"),
        "introText": introText,
        "additionalInfo": additionalInfo,
        "isActive": isActive,
    }

    # Add the new content to our 'database' about_entries
    about_entries.append(new_content)

    # Redirect back to the CMS after adding the content
    return redirect(url_for("cms.about_manager"))