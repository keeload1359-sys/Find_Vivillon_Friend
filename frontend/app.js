const { createClient } = supabase;

const supabaseClient = createClient(
    SUPABASE_URL,
    SUPABASE_PUBLISHABLE_KEY
);

const loginButton =
    document.getElementById("login-button");

const emailInput =
    document.getElementById("email");

const passwordInput =
    document.getElementById("password");

const vivillonForm =
    document.getElementById("vivillon-form");

let userId = null;
let currentTargets = [];

loginButton.addEventListener(
    "click",
    async function () {
        const email = emailInput.value;
        const password = passwordInput.value;

        const { data, error } = 
            await supabaseClient.auth.signInWithPassword({
                email: email,
                password: password
            });
        
        if (error) {
            console.log(error);
            return;
        }
        
        userId = data.user.id;
        
        const { data: targets, error:targetsError }  =
            await supabaseClient
                .from("target_vivillons")
                .select("vivillon_code")
                .eq("user_id", userId)
        
        if (targetsError) {
            console.log(targetsError);
            return;
        }
        
        currentTargets = targets;
        
        const checkboxes =
            document.querySelectorAll(".vivillon-checkbox");

        checkboxes.forEach(
            function(checkbox){

                const TargetVivillons = 
                    targets.some(
                        function(target){
                            return target.vivillon_code === checkbox.value;
                        }
                    );

                checkbox.checked = TargetVivillons;
            }
        );
    }
);

vivillonForm.addEventListener(
    "submit",
    async function (event) {
        
        event.preventDefault();

        const Checked =
            document.querySelectorAll(".vivillon-checkbox:checked");
        
        const newTargetVivillons= [];
        
        Checked.forEach(
            function(checkbox){
                newTargetVivillons.push(checkbox.value)
            }
        );

        const oldTargetVivillons = [];

        currentTargets.forEach(
            function (target) {
                oldTargetVivillons.push(
                    target.vivillon_code
                );
            }
        );

        const addedVivillons = 
            newTargetVivillons.filter(
                function(vivillon){
                    return !oldTargetVivillons.includes(vivillon)
                }
            )
        
        console.log(
            "追加対象:",
            addedVivillons
        );
        
        const removedVivillons = 
            oldTargetVivillons.filter(
                function(vivillon){
                    return !newTargetVivillons.includes(vivillon)
                }
            )
        
        console.log(
            "削除対象:",
            removedVivillons
        );
        
        for (const vivillon of addedVivillons){
            const { error: insertError } =
                await supabaseClient
                    .from("target_vivillons")
                    .insert({
                        user_id: userId,
                        vivillon_code: vivillon                
                    });

            if (insertError) {
                console.log(
                    vivillon,
                    insertError
                );
                return;
            }
        }

        for (const vivillon of removedVivillons){
            const { error: deleteError } =
                await supabaseClient
                    .from("target_vivillons")
                    .delete()
                    .eq("user_id", userId)
                    .eq("vivillon_code", vivillon);             

            if (deleteError) {
                console.log(
                    vivillon,
                    deleteError
                );
                return;
            }
        }


        const { data: latesttargets, error:latesttargetsError }  =
            await supabaseClient
                .from("target_vivillons")
                .select("vivillon_code")
                .eq("user_id", userId)
        
        if (latesttargetsError) {
            console.log(
                latesttargetsError
            );
            return;
        }
        
        
        currentTargets = latesttargets;

        console.log(
            "currentTargets最新化:",
            currentTargets
        );
        
    }
)
