const form = document.getElementById("uploadForm");
const imageInput = document.getElementById("imageInput");
const message = document.getElementById("message");
const gallery = document.getElementById("gallery");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const file = imageInput.files[0];
    if (!file) {
        message.textContent = "Please select a file.";
        return;
    }

    const formData = new FormData();
    formData.append("image", file);

    try {
        const response = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (response.ok) {
            message.textContent = data.message;

            const newCard = document.createElement("div");
            newCard.className = "card";
            newCard.id = `image-${data.id}`;

            const img = document.createElement("img");
            img.src = `/static/uploads/${data.filename}`;

            const deleteBtn = document.createElement("button");
            deleteBtn.className = "btndelete";
            deleteBtn.dataset.id = data.id;
            deleteBtn.textContent = "Delete";

            newCard.appendChild(img);
            newCard.appendChild(deleteBtn);
            gallery.prepend(newCard);

            form.reset();
        } else {
            message.textContent = data.error;
        }

    } catch (error) {
        console.error(error);
        message.textContent = "Upload failed.";
    }
});

// Event delegation for delete buttons (works for existing + dynamically added cards)
gallery.addEventListener("click", (e) => {
    if (e.target.classList.contains("btndelete")) {
        const id = e.target.dataset.id;
        deleteImage(id);
    }
});

function deleteImage(id) {
    if (!confirm("Are you sure you want to delete this image?")) {
        return;
    }

    fetch(`/delete/${id}`, {
        method: "DELETE"
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            document.getElementById(`image-${id}`).remove();
        } else {
            alert("Failed to delete image.");
        }
    })
    .catch(error => {
        console.error(error);
        alert("An error occurred while deleting the image.");
    });
}