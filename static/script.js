// Form ni select chestunnam
const form = document.getElementById("studentForm");

// Student list table
const studentList = document.getElementById("studentList");


// Students ni database nundi get cheyyadam
function loadStudents() {

    fetch("/students")
        .then(response => response.json())

        .then(students => {

            studentList.innerHTML = "";

            students.forEach(student => {

                const row = `
                    <tr>

                        <td>${student.id}</td>

                        <td>${student.name}</td>

                        <td>${student.age}</td>

                        <td>${student.course}</td>

                        <td>${student.email}</td>

                        <td>

                            <button
                                class="delete-btn"
                                onclick="deleteStudent(${student.id})">

                                Delete

                            </button>

                        </td>

                    </tr>
                `;

                studentList.innerHTML += row;

            });

        });
}


// Add Student
form.addEventListener("submit", function(event) {

    event.preventDefault();


    // Form values tiskuntunnam

    const student = {

        name: document.getElementById("name").value,

        age: document.getElementById("age").value,

        course: document.getElementById("course").value,

        email: document.getElementById("email").value

    };


    // Backend ki data pampistunnam

    fetch("/students", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(student)

    })

    .then(response => response.json())

    .then(data => {

        alert(data.message);

        form.reset();

        loadStudents();

    });

});


// Delete Student
function deleteStudent(id) {

    fetch("/students/" + id, {

        method: "DELETE"

    })

    .then(response => response.json())

    .then(data => {

        alert(data.message);

        loadStudents();

    });

}


// Page open ayyinappudu students load cheyyali
loadStudents();
